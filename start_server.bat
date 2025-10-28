@echo off
echo 🎨 Color Changer Tool - Starting Server...
echo ================================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo 💡 Please install Python from https://python.org
    echo 💡 Or use VS Code Live Server extension instead
    pause
    exit /b 1
)

echo ✅ Python found, starting server...
echo.
echo 🌐 This will open your browser automatically
echo ⏹️  Press Ctrl+C to stop the server
echo.

REM Start the Python server
python start_server.py

pause