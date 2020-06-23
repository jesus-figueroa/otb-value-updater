@echo off
:loop
cd /d %~dp0
valueupdater.exe
START "olympian.exe" olympian.exe
timeout /t 5400
taskkill /f /im "olympian.exe"
goto loop 