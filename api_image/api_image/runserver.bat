:: Django run project stript
:: Load fixtures should be run after initialize Venv, but in this path i had error

::  cmd /k "cd /d  %~dp0..\env\Scripts & activate  & cd /d  %~dp0 & py .\manage.py cmd_fixtures  %~dp0 & py manage.py runserver"^

:: this script should work if you have Python installed in, Windows with is need to create Venv  enviroment.

@echo off
py .\manage.py cmd_fixtures

cmd /k "cd /d  %~dp0..\env\Scripts & activate  & cd /d  %~dp0 & py manage.py runserver"^


