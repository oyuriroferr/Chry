@echo off
setlocal enabledelayedexpansion

:: Função para verificar e executar a primeira versão encontrada
set "python_exe="

:: Verifica no APPDATA (incluindo Roaming e Local)
set "appdata_path=%APPDATA%\Roaming\Python\Python*"
for /d %%D in (%appdata_path%) do (
    echo Verificando em APPDATA: %%D
    if exist "%%D\python.exe" (
        set "python_exe=%%D\python.exe"
        goto execute
    )
)

:: Verifica no LOCALAPPDATA (corrigido para verificar diretórios exatos)
echo Verificando em LOCALAPPDATA:
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    echo Encontrado em: %LOCALAPPDATA%\Programs\Python\Python313
    set "python_exe=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    goto execute
)

if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    echo Encontrado em: %LOCALAPPDATA%\Programs\Python\Python310
    set "python_exe=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    goto execute
)

:: Verifica no PROGRAMFILES
echo Verificando em PROGRAMFILES:
for /d %%D in ("%PROGRAMFILES%\Python*\") do (
    echo Verificando em: %%D
    if exist "%%D\python.exe" (
        set "python_exe=%%D\python.exe"
        goto execute
    )
)
for /d %%D in ("%ProgramFiles(x86)%\Python*\") do (
    echo Verificando em: %%D
    if exist "%%D\python.exe" (
        set "python_exe=%%D\python.exe"
        goto execute
    )
)

:: Se não encontrou Python no APPDATA, LOCALAPPDATA ou PROGRAMFILES
echo Nenhuma versão do Python encontrada em APPDATA, LOCALAPPDATA ou PROGRAMFILES.
echo Verifique se o Python está instalado nas pastas AppData\Roaming, AppData\Local\Programs ou Program Files.
echo.

:: Verifica no PATH
echo Verificando no PATH:
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
echo Nenhuma versão do Python encontrada no PATH.
echo Tente adicionar o Python ao seu PATH ou verifique se ele está instalado corretamente.
echo.

:: Se nenhuma versão do Python for encontrada
echo Nenhuma versão do Python foi encontrada no sistema.
exit /b

:execute
:: Executa o script com a primeira versão encontrada
echo Python encontrado: !python_exe!
"!python_exe!" initv.py
exit /b
