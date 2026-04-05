@echo off
REM Setup script for Windows

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  Sentiment Analysis API - Setup Script (Windows)             ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║  Setup Complete! ✓                                           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo To start the server, run:
echo   venv\Scripts\activate.bat
echo   python main.py
echo.
echo Then open http://localhost:8000/docs in your browser
echo.
pause
