# Big Picture Trading — Video to Transcript Procedure

## One-time setup

```powershell
pip install -U yt-dlp faster-whisper
conda install -c conda-forge ffmpeg
```

Disable Windows sleep on AC (so unattended transcriptions don't pause):

```powershell
powercfg /change standby-timeout-ac 0
powercfg /change monitor-timeout-ac 0
```

(Restore later with `powercfg /change standby-timeout-ac 30` if desired.)

Allow PowerShell to run local scripts (one-time):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Verify:

```powershell
yt-dlp --version
ffmpeg -version
```

Place these files in the same directory (e.g. `C:\Users\aldoh\Documents\Transcripts\`):

- `Run-Transcribe.ps1` — orchestration wrapper
- `transcribe.py` — Whisper transcription script

## Recurring procedure

### Step 1 — Get the Vimeo video ID

1. Open the video page in Firefox (logged in)
2. Press **F12** → **Inspecteur** tab
3. Expand `<body>` → expand `<div style="padding:75% 0 0...">`
4. Find the `<iframe src="https://player.vimeo.com/video/[ID]?...">`
5. Copy the numeric ID (e.g. `1189778472`)

### Step 2 — Run the wrapper

One command does everything: download audio, queue behind any running transcription, then transcribe.

```powershell
.\Run-Transcribe.ps1 1189778472 20260506
```

The wrapper will:

1. Check for running `transcribe.py` processes — if any, queue this run after them
2. Download the audio with yt-dlp (skipped if already on disk)
3. Wait for prior runs to finish (if any)
4. Run `transcribe.py` and produce `wherestrade_<date>_transcript.txt`
5. Summarize it into `wherestrade_<date>_summary.md` via the headless `claude` CLI
   (the project `/transcribe` command, summarize-only mode), `--permission-mode acceptEdits`

### Step 3 — Summarize (now automatic)

The wrapper runs the summary itself (step 5 above) — no manual upload needed. It
invokes `claude -p "/transcribe wherestrade_<date>_transcript.txt" --permission-mode acceptEdits`
from the `Transcripts` directory, producing `wherestrade_<date>_summary.md` (narrative
+ every-ticker table + notable levels, per the `/transcribe` command spec).

- Pass `-SkipSummary` to produce the transcript only.
- If the summary step is skipped or fails (e.g. `claude` not on PATH), the transcript
  is intact; summarize later with:
  `claude -p "/transcribe wherestrade_<date>_transcript.txt" --permission-mode acceptEdits`

---

## Wrapper options

```powershell
# Standard run
.\Run-Transcribe.ps1 1189778472 20260506

# Download only (transcribe later)
.\Run-Transcribe.ps1 1189778472 20260506 -SkipTranscribe

# Transcribe only (audio already downloaded)
.\Run-Transcribe.ps1 1189778472 20260506 -SkipDownload

# Named parameters (equivalent to positional)
.\Run-Transcribe.ps1 -VideoId 1189778472 -Date 20260506
```

---

## Queueing multiple videos

The wrapper auto-detects running transcriptions, so you can just fire-and-forget — open a second PowerShell window and launch the next one:

```powershell
.\Run-Transcribe.ps1 1190000000 20260507
```

It will detect the running PID from the first run and wait for it before starting transcription. The download still happens immediately (it's just yt-dlp, no GPU/CPU contention).

---

## Troubleshooting

- **yt-dlp redirects to login page**: use the `player.vimeo.com/video/[ID]` URL with `--referer`, not the Big Picture page URL.
- **"format ba not available"**: run `yt-dlp -F` to list formats, pick highest audio-only ID with `-f 234` (or whatever number).
- **"running this script is disabled"**: run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` (one-time).
- **ffmpeg not found during transcription**: `conda install -c conda-forge ffmpeg` and reopen PowerShell.
- **First run of transcribe.py is slow to start**: ~3 GB model download, one-time only, cached in `~/.cache/huggingface/`.
- **Transcription stalls during sleep**: ensure `powercfg /change standby-timeout-ac 0` was run before leaving the machine unattended.
- **Wrapper can't find transcribe.py**: both files must be in the same directory. The wrapper uses `$PSScriptRoot` to locate `transcribe.py`.
