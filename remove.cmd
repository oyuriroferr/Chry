@echo off

:: Lê o caminho do Python do arquivo python.txt
set /p DIR=<"%USERPROFILE%\Portable\python.txt"

:: Verifica se a pasta venv existe
if exist "%USERPROFILE%\Portable\venv\" (
    :: Deleta a pasta Portable
    RD /S /Q "%USERPROFILE%\Portable"
    echo Venv Version
    :: Verifica se houve erro ao excluir o diretório
    if %errorlevel% NEQ 0 (
        echo Erro ao Deletar Venv Version
    )
) else (
    :: Desinstala os pacotes globalmente
    "%DIR%" -m pip uninstall -y pywin32 pynput pygame pyautogui psutil ffpyplayer pywin32 
    :: Deleta a pasta Portable
    RD /S /Q "%USERPROFILE%\Portable"
    echo Global Version
    :: Verifica se houve erro ao excluir o diretório
    if %errorlevel% NEQ 0 (
        echo Erro ao Deletar Global Version
    )
)

pause
