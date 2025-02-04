import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo de áudio
pygame.mixer.music.load('audio.mp3')

# Tocar o áudio em loop indefinido
pygame.mixer.music.play(-1)

# Manter o programa em execução para que o áudio toque
while True:
    pass
