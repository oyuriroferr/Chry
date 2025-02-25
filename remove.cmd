@echo off

:: Lê o caminho do Python do arquivo python.txt
set /p DIR=<"%USERPROFILE%\Portable\python.txt"

:: Verifica se a variável DIR está vazia
if "%DIR%"=="" (
    cls
    echo Nao foi possivel achar o caminho do Python
    goto end_bad
)

:: Verifica se a pasta venv existe
if exist "%USERPROFILE%\Portable\venv\" (
    :: Deleta a pasta Portable
    cls
    RD /S /Q "%USERPROFILE%\Portable"
    echo Venv Version Deleted
    goto end_good
)

:: Se não encontrou a pasta venv, verifica a pasta Portable
if exist "%USERPROFILE%\Portable\" (
    :: Desinstala os pacotes globalmente
    cls
    "%DIR%" -m pip uninstall -y pywin32 pynput pygame pyautogui psutil ffpyplayer pywin32
    :: Deleta a pasta Portable
    RD /S /Q "%USERPROFILE%\Portable"
    echo Global Version Deleted
    goto end_good
)

:end_good
echo Goodbye!!!
pause

:end_bad
echo Fudeu nego!
pause
