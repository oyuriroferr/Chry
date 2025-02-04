@echo off
setlocal enabledelayedexpansion

REM Verifica se o arquivo pip.exe existe
if exist "%userprofile%\AppData\Roaming\Python\Python313\Scripts\pip.exe" (
    echo pip.exe encontrado, removendo os pacotes...
    "%userprofile%\AppData\Roaming\Python\Python313\Scripts\pip.exe" uninstall pywin32 pynput pygame pyautogui -y
    if errorlevel 1 (
        echo Erro ao executar o pip. Verifique a instalação.
    )
) else (
    echo pip.exe nao encontrado.
)

:: Obtém o caminho do diretório do usuário atual
set USER_DIR=%USERPROFILE%

:: Define os caminhos
set DESTINATION=%USER_DIR%\Portable

:: Remove a pasta Portable e todo seu conteúdo
if exist "%DESTINATION%" (
    echo Removendo a pasta Portable e seu conteúdo...
    rmdir /S /Q "%DESTINATION%"
    if errorlevel 1 (
        echo Erro ao remover a pasta Portable.
        pause
        exit /b
    )
    echo Pasta Portable removida com sucesso.
) else (
    echo A pasta Portable nao foi encontrada.
)

pause
