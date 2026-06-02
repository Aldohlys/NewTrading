<#
.SYNOPSIS
    Big Picture Trading transcription pipeline wrapper.

.DESCRIPTION
    Downloads audio from a Vimeo video, transcribes it, then summarizes the
    transcript into <root>_<date>_summary.md via the headless `claude` CLI
    (the project /transcribe command, summarize-only mode).
    If another python.exe (transcribe.py) is already running, automatically
    queues this run to start after it finishes.

.PARAMETER SkipSummary
    Skip the Claude summarization step (produce the transcript .txt only).

.PARAMETER VideoId
    The Vimeo numeric video ID (from the iframe src in the page DOM).

.PARAMETER Date
    Date in YYYYMMDD format. Used for filenames.

.PARAMETER SkipDownload
    Skip the yt-dlp download step (audio file already on disk).

.PARAMETER SkipTranscribe
    Skip the transcription step (download only).

.EXAMPLE
    .\Run-Transcribe.ps1 -VideoId 1189778472 -Date 20260506

.EXAMPLE
    .\Run-Transcribe.ps1 1189778472 20260506

.EXAMPLE
    # Download only, transcribe later
    .\Run-Transcribe.ps1 1189778472 20260506 -SkipTranscribe
#>

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$VideoId,

    [Parameter(Mandatory=$true, Position=1)]
    [ValidatePattern('^\d{8}$')]
    [string]$Date,

    [switch]$SkipDownload,
    [switch]$SkipTranscribe,
    [switch]$SkipSummary
)

$ErrorActionPreference = "Stop"

# --- Config ---------------------------------------------------------------
$Referer       = "https://secure.bigpicturetrading.com/"
$AudioPattern  = "audio_$Date"
$TranscriptOut = "wherestrade_${Date}_transcript.txt"
$ScriptDir     = $PSScriptRoot
$TranscribePy  = Join-Path $ScriptDir "transcribe.py"

# Anchor CWD to the script's own directory so audio + transcript land in
# Transcripts\, no matter where the caller invoked us from (bash mangles
# Windows paths in `cd C:\...\Transcripts`, which would otherwise fail).
Set-Location -LiteralPath $ScriptDir

# --- Helpers --------------------------------------------------------------
function Write-Step {
    param([string]$Message)
    Write-Host ""
    Write-Host "=== $Message ===" -ForegroundColor Cyan
}

function Find-AudioFile {
    param([string]$Pattern)
    $extensions = @("mp4", "m4a", "webm", "opus")
    foreach ($ext in $extensions) {
        $candidate = "$Pattern.$ext"
        if (Test-Path $candidate) {
            return $candidate
        }
    }
    return $null
}

function Get-RunningTranscriptions {
    # Find python processes running transcribe.py
    Get-CimInstance Win32_Process -Filter "Name = 'python.exe'" |
        Where-Object { $_.CommandLine -match 'transcribe\.py' } |
        Select-Object ProcessId, CommandLine, CreationDate
}

# --- 1. Check for running transcriptions and queue if needed --------------
$pidsToWait = @()

if (-not $SkipTranscribe) {
    Write-Step 'Checking for running transcriptions'
    $running = Get-RunningTranscriptions

    if ($running) {
        Write-Host 'Found running transcription(s):' -ForegroundColor Yellow
        $running | ForEach-Object {
            Write-Host "  PID $($_.ProcessId): $($_.CommandLine)" -ForegroundColor Yellow
        }

        $pidsToWait = @($running | Select-Object -ExpandProperty ProcessId)
        Write-Host ''
        Write-Host "Will wait for PID(s) $($pidsToWait -join ', ') to exit before starting." -ForegroundColor Yellow
    } else {
        Write-Host 'No running transcriptions detected.' -ForegroundColor Green
    }
}

# --- 2. Download audio with yt-dlp ----------------------------------------
if (-not $SkipDownload) {
    Write-Step "Downloading audio for video $VideoId"

    $existing = Find-AudioFile -Pattern $AudioPattern
    if ($existing) {
        Write-Host "Audio file already exists: $existing - skipping download." -ForegroundColor Green
    } else {
        $vimeoUrl = "https://player.vimeo.com/video/$VideoId"
        $outputTemplate = "$AudioPattern.%(ext)s"

        Write-Host "URL: $vimeoUrl"
        Write-Host "Output: $outputTemplate"

        & yt-dlp -f ba --referer $Referer $vimeoUrl -o $outputTemplate
        if ($LASTEXITCODE -ne 0) {
            throw "yt-dlp failed with exit code $LASTEXITCODE"
        }
    }
} else {
    Write-Host 'Skipping download (-SkipDownload set).' -ForegroundColor Yellow
}

# --- 3. Verify audio file exists ------------------------------------------
if (-not $SkipTranscribe) {
    $audioFile = Find-AudioFile -Pattern $AudioPattern
    if (-not $audioFile) {
        throw "No audio file found matching $AudioPattern.* - cannot transcribe."
    }
    Write-Host "Audio file: $audioFile" -ForegroundColor Green
}

# --- 4. Wait for any prior runs, then transcribe --------------------------
if (-not $SkipTranscribe) {
    if ($pidsToWait.Count -gt 0) {
        Write-Step 'Waiting for prior transcription(s) to finish'
        foreach ($waitPid in $pidsToWait) {
            try {
                Wait-Process -Id $waitPid -ErrorAction Stop
                Write-Host "PID $waitPid finished." -ForegroundColor Green
            } catch {
                Write-Host "PID $waitPid already exited." -ForegroundColor Green
            }
        }
    }

    Write-Step 'Transcribing'
    if (-not (Test-Path $TranscribePy)) {
        throw "transcribe.py not found at $TranscribePy"
    }

    & python $TranscribePy $VideoId $Date
    if ($LASTEXITCODE -ne 0) {
        throw "transcribe.py failed with exit code $LASTEXITCODE"
    }

    Write-Step 'Done'
    if (Test-Path $TranscriptOut) {
        $size = (Get-Item $TranscriptOut).Length
        Write-Host "Transcript: $TranscriptOut ($([math]::Round($size/1KB, 1)) KB)" -ForegroundColor Green
    }
} else {
    Write-Host 'Skipping transcription (-SkipTranscribe set).' -ForegroundColor Yellow
}

# --- 5. Summarize via headless Claude -------------------------------------
# Runs the project /transcribe command in summarize-only mode on the produced
# transcript (it resolves the single existing-file arg -> writes
# <root>_<date>_summary.md). cwd is already $ScriptDir (Transcripts), so both
# the .claude/commands/transcribe.md command and the transcript file resolve.
# --permission-mode acceptEdits lets it write the summary unattended.
# Non-fatal: if the summary step fails, the transcript is still on disk and can
# be summarized later with `claude -p "/transcribe <transcript>"`.
if (-not $SkipSummary) {
    Write-Step 'Summarizing transcript (headless Claude)'
    $SummaryOut = "wherestrade_${Date}_summary.md"

    if (-not (Test-Path $TranscriptOut)) {
        Write-Host "Transcript $TranscriptOut not found - skipping summary." -ForegroundColor Yellow
    } elseif (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
        Write-Host "claude CLI not on PATH - skipping summary." -ForegroundColor Yellow
        Write-Host "  Summarize later with: claude -p `"/transcribe $TranscriptOut`" --permission-mode acceptEdits" -ForegroundColor Yellow
    } else {
        Write-Host "Running: claude -p `"/transcribe $TranscriptOut`" --permission-mode acceptEdits"
        & claude -p "/transcribe $TranscriptOut" --permission-mode acceptEdits
        $claudeExit = $LASTEXITCODE

        if ($claudeExit -ne 0) {
            Write-Host "claude exited $claudeExit - transcript is intact; re-run the summary later." -ForegroundColor Yellow
        } elseif (Test-Path $SummaryOut) {
            $ssz = (Get-Item $SummaryOut).Length
            Write-Host "Summary: $SummaryOut ($([math]::Round($ssz/1KB, 1)) KB)" -ForegroundColor Green
        } else {
            Write-Host "claude finished but $SummaryOut was not created - check the output above." -ForegroundColor Yellow
        }
    }
} else {
    Write-Host 'Skipping summary (-SkipSummary set).' -ForegroundColor Yellow
}
