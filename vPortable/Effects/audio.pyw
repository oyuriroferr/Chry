import pygame
from subprocess import Popen
from time import sleep
sleep(0.8)
# AUMENTA O VOLUME USANDO O POWERSHELL (Simula pressionamento de teclas)
Popen(r'powershell -c "$wshell = New-Object -ComObject WScript.Shell; 1..50 | ForEach-Object { $wshell.SendKeys([char]175) }"',shell=True)


# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo de áudio
pygame.mixer.music.load('audio.mp3')

# Tocar o áudio em loop indefinido
pygame.mixer.music.play(-1)

# Manter o programa em execução para que o áudio toque
while True:
    pass
