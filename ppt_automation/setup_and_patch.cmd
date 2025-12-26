@echo off
setlocal

REM Move to this script's directory
cd /d %~dp0

echo === PPT Auto-Patcher ===

REM Create venv if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate.bat

REM Upgrade pip (quietly)
python -m pip install --upgrade pip >nul

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Run patcher
echo Running PowerPoint patcher...
python patch_pptx.py input\output.pptx

echo.
echo ✓ Done. You can close this window.
pause
