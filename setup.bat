@echo off
REM Setup script for AI Booking Assistant
REM Run this on Windows to set up everything

echo.
echo ===================================
echo AI Booking Assistant - Setup
echo ===================================
echo.

REM Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Created: venv/
) else (
    echo Already exists: venv/
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [4/4] Creating .env file from template...
if not exist .env (
    copy .env.example .env
    echo Created: .env
    echo.
    echo IMPORTANT: Edit .env and add your LLM API key!
    echo.
) else (
    echo Already exists: .env
)

echo.
echo ===================================
echo Setup complete!
echo ===================================
echo.
echo Next steps:
echo 1. Edit .env and add your LLM API key
echo 2. Run: python app.py
echo 3. Open: http://localhost:5000
echo.
pause
