@echo off
SETLOCAL EnableDelayedExpansion
title /analyze single-ticker deep dive

REM @args: TICKER DIRECTION [extras]
REM Usage: run_analyze.bat TICKER long|short [--no-html] [--no-vol-funnel] [--refresh] [--max-age <hours>]
if "%~2"=="" (
    echo Usage: run_analyze.bat TICKER long^|short [--no-html] [--no-vol-funnel] [--refresh] [--max-age ^<hours^>]
    pause
    exit /b 1
)

REM CWD must be RStudies so .Rprofile activates renv and finds Tdata
cd /d "C:\Users\aldoh\Documents\RApplication\RStudies"

for /f %%i in ('powershell -noprofile -command "Get-Date -Format yyyyMMdd"') do set TODAY=%%i

set TICKER=%~1
set DIRECTION=%~2
REM Pass-through every arg after position 2 (preserves --max-age <hours> pairs)
set EXTRA=
shift & shift
:collect_extra
if "%~1"=="" goto :run
set EXTRA=!EXTRA! %~1
shift
goto :collect_extra
:run

echo ============================================
echo  /analyze !TICKER! !DIRECTION!  ^(!TODAY!^)
echo ============================================
"C:\Program Files\R\R-4.4.3\bin\Rscript.exe" reports/analyze/main.R !TICKER! !DIRECTION! !EXTRA!
set EXIT=!ERRORLEVEL!

if !EXIT! NEQ 0 (
    echo.
    echo [ERROR] /analyze failed with exit code !EXIT!
    pause
    exit /b !EXIT!
)

REM Open the produced HTML unless --no-html was passed
echo !EXTRA! | findstr /c:"--no-html" >nul
if !ERRORLEVEL! NEQ 0 start "" "C:\Users\aldoh\Documents\NewTrading\reports\analyze_!TICKER!_!TODAY!.html"

echo.
echo ============================================
echo  DONE
echo ============================================
pause
