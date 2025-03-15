@echo off
setlocal enabledelayedexpansion
call :setESC
cls
echo %ESC%[31m* CMD

:: Função para verificar e executar a primeira versão encontrada
set "python_exe="

:: Verifica no APPDATA (incluindo Roaming e Local)
set "appdata_path=%APPDATA%\Roaming\Python\Python*"
for /d %%D in (%appdata_path%) do (
    echo %ESC%[31mVerificando em APPDATA: %%D
    if exist "%%D\python.exe" (
        set "python_exe=%%D\python.exe"
        goto execute
    )
)

:: Verifica no LOCALAPPDATA (corrigido para verificar diretórios exatos)
echo %ESC%[31mVerificando em LOCALAPPDATA 3.(13,10,9):
if exist "%LOCALAPPDATA%\Programs\Python\Python39\python.exe" (
    echo %ESC%[31mEncontrado em: %LOCALAPPDATA%\Programs\Python\Python39
    set "python_exe=%LOCALAPPDATA%\Programs\Python\Python39\python.exe"
    goto execute
)
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    echo %ESC%[31mEncontrado em: %LOCALAPPDATA%\Programs\Python\Python313
    set "python_exe=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    goto execute
)

if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    echo %ESC%[31mEncontrado em: %LOCALAPPDATA%\Programs\Python\Python310
    set "python_exe=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    goto execute
)
:: Verifica no LOCALAPPDATA ETEC
if exist "%programfiles%\Python39\python.exe" (
    echo %ESC%[31mEncontrado em:%programfiles%\Python39\python.exe
    set "python_exe=%programfiles%\Python39\python.exe"
    goto execute
)
:: ETEC NOVOS
if exist "%programfiles%\Python313\python.exe" (
    echo %ESC%[31mEncontrado em:%programfiles%\Python313\python.exe
    set "python_exe=%programfiles%\Python313\python.exe"
    goto execute
)

:: Verifica no PROGRAMFILES
echo %ESC%[31mVerificando em PROGRAMFILES:
for /d %%D in ("%PROGRAMFILES%\Python***\") do (
    echo %ESC%[31mVerificando em: %%D
    if exist "%%D\python.exe" (
        set "python_exe=%%D\python.exe"
        goto execute
    )
)
for /d %%D in ("%ProgramFiles(x86)%\Python*\") do (
    echo %ESC%[31mVerificando em: %%D
    if exist "%%D\python.exe" (
        set "python_exe=%%D\python.exe"
        goto execute
    )
)

:: Se não encontrou Python no APPDATA, LOCALAPPDATA ou PROGRAMFILES
echo %ESC%[31mNenhuma versão do Python encontrada em APPDATA, LOCALAPPDATA ou PROGRAMFILES.
echo %ESC%[31mVerifique se o Python está instalado nas pastas AppData\Roaming, AppData\Local\Programs ou Program Files.
echo.

:: Verifica no PATH
echo %ESC%[31mVerificando no PATH:
for %%P in ("python" "python3") do (
    where /R C:\ %%P.exe >nul 2>nul
    if !errorlevel! == 0 (
        for /f %%i in ('where %%P.exe') do (
            set "python_exe=%%i"
            goto execute
        )
    )
)


:: Se não encontrou Python no PATH
echo %ESC%[31mNenhuma versão do Python encontrada no PATH.
echo %ESC%[31mTente adicionar o Python ao seu PATH ou verifique se ele está instalado corretamente.
echo.

:: Se nenhuma versão do Python for encontrada
echo %ESC%[31mNenhuma versão do Python foi encontrada no sistema.
exit /b

:execute
:: Executa o script com a primeira versão encontrada
echo %ESC%[31mPython encontrado: !python_exe!%ESC%[0m
echo !python_exe!>python_path.txt
"!python_exe!" initv.py
::powershell -NoExit -NoProfile -ExecutionPolicy Bypass -Command "& '!python_exe!' 'initv.py'"


:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /b
