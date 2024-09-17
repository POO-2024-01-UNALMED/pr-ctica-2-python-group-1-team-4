@echo off
:: Minimiza la ventana de CMD
powershell -windowstyle hidden -command ""

cd /d "%~dp0"
python src//uiMain//vent_inicio.py

pause
