@echo off
:loop
cd /d %~dp0
valueupdater.exe
START "olympian.exe" olympian.exe
REM You can change restart time by editing the value below, its in seconds
timeout /t 3600
taskkill /f /im "olympian.exe"
goto loop 
