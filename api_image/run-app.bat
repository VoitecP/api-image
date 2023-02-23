@Echo Off

Set "VIRTUAL_ENV=env"

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    pip.exe install virtualenv
    python.exe -m venv %VIRTUAL_ENV%
)

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" Exit /B 1

Call "%VIRTUAL_ENV%\Scripts\activate.bat"
cd /d  %~dp0api_image\

pip.exe install -r requirements.txt

::@py.exe
python manage.py cmd_fixtures
::@py.exe
python manage.py runserver

Pause
Exit /B 0


