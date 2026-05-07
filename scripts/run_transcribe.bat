@echo off
SETLOCAL EnableDelayedExpansion
title Big Picture Trading transcription

REM @args: VIDEO_ID YYYYMMDD [flags]
REM Usage: run_transcribe.bat VIDEO_ID YYYYMMDD [-SkipDownload] [-SkipTranscribe]
if "%~2"=="" (
    echo Usage: run_transcribe.bat VIDEO_ID YYYYMMDD [-SkipDownload] [-SkipTranscribe]
    pause
    exit /b 1
)

REM CWD = Transcripts so audio/transcript files land next to the script
cd /d "C:\Users\aldoh\Documents\NewTrading\Transcripts"

powershell -NoProfile -ExecutionPolicy Bypass -File ".\Run-Transcribe.ps1" %*
set EXIT=!ERRORLEVEL!

if !EXIT! NEQ 0 (
    echo.
    echo [ERROR] Run-Transcribe.ps1 failed with exit code !EXIT!
    pause
    exit /b !EXIT!
)

echo.
echo ============================================
echo  DONE
echo ============================================
pause
