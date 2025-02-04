import win32gui
import time
import random
import threading

# Função de callback para processar cada janela
def enum_windows_callback(hwnd, windows):
    if win32gui.IsWindowVisible(hwnd):  # Verifica se a janela está visível
        window_text = win32gui.GetWindowText(hwnd)
        if window_text:  # Verifica se a janela tem um título
            windows.append((hwnd, window_text))

# Função para obter todas as janelas abertas
def get_open_windows():
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows

# Função para mover uma janela aleatoriamente
def move_window_randomly(hwnd, title):
    
#    for _ in range(100):  # Número de movimentos
    while True:
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        win32gui.MoveWindow(hwnd, x, y, 800, 600, True)
        time.sleep(0.1)

# Lista todas as janelas abertas
open_windows = get_open_windows()



# Cria uma thread para cada janela
threads = []
for hwnd, title in open_windows:
    t = threading.Thread(target=move_window_randomly, args=(hwnd, title))
    threads.append(t)
    t.start()

# Aguarda todas as threads terminarem
for t in threads:
    t.join()
