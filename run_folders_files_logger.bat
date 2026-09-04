@echo off
cd /d "%~dp0"
where pythonw >nul 2>nul
if %errorlevel%==0 (
    pythonw "%~dp0folders_files_logger.py"
) else (
    python "%~dp0folders_files_logger.py"
)
