@echo off
echo.
echo.
echo                   **********************************
echo                   *                                *
echo                   *            ScalesAPI           *
echo                   *                                *
echo                   **********************************
echo.
echo.
echo Starting ScalesAPI...
echo Activating venv...
call %~dp0\venv\Scripts\activate.bat
echo venv activated successfully
echo Call main.py
call python %~dp0\main.py
pause
