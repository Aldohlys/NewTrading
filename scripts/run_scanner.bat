@echo off
SETLOCAL EnableDelayedExpansion
title Macro Context + Swing Scanner
REM CWD must be the renv-activated project root (RStudies) so that .Rprofile
REM sources renv/activate.R and Rscript picks up RStudies' Tdata (5.10.4+),
REM not the default R library (which may be months out of date).
cd /d "C:\Users\aldoh\Documents\RApplication\RStudies"

REM Get today's date as YYYYMMDD
for /f %%i in ('powershell -noprofile -command "Get-Date -Format yyyyMMdd"') do set TODAY=%%i

echo ============================================
echo  MACRO CONTEXT REPORT
echo ============================================
"C:\Program Files\R\R-4.4.3\bin\Rscript.exe" reports/macro_context/main.R
set MACRO_EXIT=!ERRORLEVEL!
if !MACRO_EXIT! NEQ 0 (
    echo.
    echo [ERROR] macro_context failed with exit code !MACRO_EXIT!
    pause
    exit /b 1
)
start "" "C:\Users\aldoh\Documents\NewTrading\reports\macro_context_%TODAY%.html"

REM Brief pause to let SQLite release file lock
timeout /t 2 /nobreak >nul

echo.
echo ============================================
echo  SWING SCANNER (front-run option flow)
echo ============================================
"C:\Program Files\R\R-4.4.3\bin\Rscript.exe" reports/swing_scanner/main.R
set SCANNER_EXIT=!ERRORLEVEL!
if !SCANNER_EXIT! NEQ 0 (
    echo.
    echo [ERROR] swing_scanner failed with exit code !SCANNER_EXIT!
    pause
    exit /b 1
)
start "" "C:\Users\aldoh\Documents\NewTrading\reports\swing_scanner_%TODAY%.html"

echo.
echo ============================================
echo  DONE
echo ============================================
pause
