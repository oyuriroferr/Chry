import win32gui
import win32con
import ctypes
import threading
import random
from time import sleep

# Obtém as dimensões da tela
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Estrutura para MessageBox personalizada
class MSGBOXPARAMS(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("hwndOwner", ctypes.c_void_p),
        ("hInstance", ctypes.c_void_p),
        ("lpszText", ctypes.c_wchar_p),
        ("lpszCaption", ctypes.c_wchar_p),
        ("dwStyle", ctypes.c_uint),
        ("lpszIcon", ctypes.c_wchar_p),
        ("dwContextHelpId", ctypes.c_void_p),
        ("lpfnMsgBoxCallback", ctypes.c_void_p),
        ("dwLanguageId", ctypes.c_uint)
    ]

def spam_dialog():
    title = "Chry"
    messages_bx = ["b7b6f15395d6c8f341ce6220fedf522019df0a66a8209420607a9e0bc86c6e00",
                   "Bin Bong BOOMMM!!!!!",
                   "ERROR 666\nTry again in another life!!",
                   "Omggggg You WIN\nTHE NOBEL Omggggg You WIN\nTHE NOBEL FOR BEING THE MOST IDIOTIC PERSON ON EARTH!!!!!!!!",
                   "Don't cry, you're just another fool.", "SLK SILVIO SANTOS, CLICOU NO LINK DO TIGRINHO É????",
                   "Eita Giovana...", "Lá vai o Marcos,\n clicando em todos os link do tigrinho",
                   "Azidéia jão, clicando nums bglho mó errado né",
                   "É a Brazino, o jogo da galera...",
                   "VISHHHH! Já era, tenta de novo na próxima vida!",
                   "ERROR 404\nVírus detectado, sua inteligência não foi encontrada!",
                   "Just kidding. You thought you'd get away that easy.",
                   "Chry is watching you.",
                   "BOOM! Everything is gone. Forever.",
                   "You shouldn't have clicked that link...",
                   "Oops! The system crashed, and it's all your fault.",
                   "Welcome to Chry. Hope you're ready for the ride.",
                   "This is just the beginning. Don't panic... too much.",
                   "Are you sure you want to continue? Because you can't go back now.",
                   "Your life choices have led you here... enjoy the chaos.",
                   "Don't worry, your computer is still working... or is it?",
                   "Would you like to play a game? Too bad, it's too late now.",
                   "The system is locked. But you're not getting out that easily.",
                   "Just when you thought you were safe... here I am.",
                   "Oops, I broke everything. Now it's your problem.",
                   "You clicked the wrong link. Now you're mine.",
                   "Don't bother trying to fix it. It's already too late.",
                   "The more you try to fix it, the worse it gets.",
                   "Congratulations! You've just been infected by Chry.",
                   "Brincadeira. Você achou que ia sair dessa tão fácil.",
                   "Chry está te observando.",
                   "BOOM! Tudo se foi. Para sempre.",
                   "Você não devia ter clicado naquele link...",
                   "Oops! O sistema travou, e é toda sua culpa.",
                   "Bem-vindo ao Chry. Espero que esteja pronto para a viagem.",
                   "Isso é só o começo. Não entre em pânico... tanto assim.",
                   "Tem certeza de que quer continuar? Porque você não pode voltar agora.",
                   "Suas escolhas de vida te trouxeram até aqui... aproveite o caos.",
                   "Não se preocupe, seu computador ainda está funcionando... ou será?",
                   "Gostaria de jogar um jogo? Que pena, já é tarde demais.",
                   "O sistema está bloqueado. Mas você não vai sair tão fácil.",
                   "Justo quando você pensava que estava seguro... aqui estou eu.",
                   "Oops, eu quebrei tudo. Agora é seu problema.",
                   "Você clicou no link errado. Agora você é meu.",
                   "Não adianta tentar consertar. Já é tarde demais.",
                   "Quanto mais você tenta consertar, pior fica.",
                   "Parabéns! Você acaba de ser infectado pelo Chry."
                   ]

    messages_bx_types = [win32con.MB_ICONEXCLAMATION, win32con.MB_ICONHAND, win32con.MB_ICONMASK, win32con.MB_ICONSTOP,
                         win32con.MB_ICONASTERISK, win32con.MB_ICONERROR, win32con.MB_ICONINFORMATION,
                         win32con.MB_ICONQUESTION, win32con.MB_ICONWARNING]

    message = random.choice(messages_bx)
    icon = random.choice(messages_bx_types)

    # Cria a estrutura para MessageBoxIndirect
    mbp = MSGBOXPARAMS()
    mbp.cbSize = ctypes.sizeof(MSGBOXPARAMS)
    mbp.lpszText = message
    mbp.lpszCaption = title
    mbp.dwStyle = icon | win32con.MB_OK

    # Exibe a MessageBox de forma NÃO BLOQUEANTE
    ctypes.windll.user32.MessageBoxIndirectW(ctypes.byref(mbp))

    # Aguarda a janela aparecer
    sleep(0.2)

    # Obtém o handle da MessageBox
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        # Gera uma posição aleatória na tela
        x = random.randint(0, screen_width - 300)
        y = random.randint(0, screen_height - 200)

        # Move a MessageBox para a posição aleatória
        win32gui.SetWindowPos(hwnd, None, x, y, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)

def start_spamming(num_threads):
    for _ in range(num_threads):
        delay = random.uniform(0.08, 0.4)  # Pequeno atraso entre as mensagens
        threading.Thread(target=spam_dialog, daemon=True).start()
        sleep(delay)

# Define a quantidade total de mensagens (aleatória entre 70 e 250)
spam = random.randint(70, 250)
counter = 0

# Configuração inicial do tempo de espera
sleep_plus = 0.5  # Começa maior e diminui gradualmente
decrease_factor = sleep_plus / spam + (sleep_plus  / spam) + 1 # Diminuição gradual baseada no total de mensagens

# Executa as mensagens de forma controlada
while counter <= spam:
    start_spamming(1)  # Envia uma MessageBox por vez
    counter += 1  # Incrementa o contador
    sleep(sleep_plus)  # Pequeno atraso para evitar sobrecarga
    sleep_plus = max(0.05, sleep_plus - decrease_factor)  # Diminui e garante um mínimo de 0.05s

"""import threading
from time import sleep
from numpy.random import randint
import win32ui
import win32con
from random import choice

def spam_dialog():
    title = "Chry"
    messages_bx = ["b7b6f15395d6c8f341ce6220fedf522019df0a66a8209420607a9e0bc86c6e00",
                   "Bin Bong BOOMMM!!!!!",
                   "ERROR 666\nTry again in another life!!",
                   "Omggggg You WIN\nTHE NOBEL Omggggg You WIN\nTHE NOBEL FOR BEING THE MOST IDIOTIC PERSON ON EARTH!!!!!!!!",
                   "Don't cry, you're just another fool.", "SLK SILVIO SANTOS, CLICOU NO LINK DO TIGRINHO É????",
                   "Eita Giovana...", "Lá vai o Marcos,\n clicando em todos os link do tigrinho",
                   "Azidéia jão, clicando nums bglho mó errado né",
                   "É a Brazino, o jogo da galera...",
                   "VISHHHH! Já era, tenta de novo na próxima vida!",
                   "ERROR 404\nVírus detectado, sua inteligência não foi encontrada!",
                   "Just kidding. You thought you'd get away that easy.",
                   "Chry is watching you.",
                   "BOOM! Everything is gone. Forever.",
                   "You shouldn't have clicked that link...",
                   "Oops! The system crashed, and it's all your fault.",
                   "Welcome to Chry. Hope you're ready for the ride.",
                   "This is just the beginning. Don't panic... too much.",
                   "Are you sure you want to continue? Because you can't go back now.",
                   "Your life choices have led you here... enjoy the chaos.",
                   "Don't worry, your computer is still working... or is it?",
                   "Would you like to play a game? Too bad, it's too late now.",
                   "The system is locked. But you're not getting out that easily.",
                   "Just when you thought you were safe... here I am.",
                   "Oops, I broke everything. Now it's your problem.",
                   "You clicked the wrong link. Now you're mine.",
                   "Don't bother trying to fix it. It's already too late.",
                   "The more you try to fix it, the worse it gets.",
                   "Congratulations! You've just been infected by Chry.",
                   "Brincadeira. Você achou que ia sair dessa tão fácil.",
                   "Chry está te observando.",
                   "BOOM! Tudo se foi. Para sempre.",
                   "Você não devia ter clicado naquele link...",
                   "Oops! O sistema travou, e é toda sua culpa.",
                   "Bem-vindo ao Chry. Espero que esteja pronto para a viagem.",
                   "Isso é só o começo. Não entre em pânico... tanto assim.",
                   "Tem certeza de que quer continuar? Porque você não pode voltar agora.",
                   "Suas escolhas de vida te trouxeram até aqui... aproveite o caos.",
                   "Não se preocupe, seu computador ainda está funcionando... ou será?",
                   "Gostaria de jogar um jogo? Que pena, já é tarde demais.",
                   "O sistema está bloqueado. Mas você não vai sair tão fácil.",
                   "Justo quando você pensava que estava seguro... aqui estou eu.",
                   "Oops, eu quebrei tudo. Agora é seu problema.",
                   "Você clicou no link errado. Agora você é meu.",
                   "Não adianta tentar consertar. Já é tarde demais.",
                   "Quanto mais você tenta consertar, pior fica.",
                   "Parabéns! Você acaba de ser infectado pelo Chry."
                   ]
    messages_bx_types = [win32con.MB_ICONEXCLAMATION, win32con.MB_ICONHAND, win32con.MB_ICONMASK, win32con.MB_ICONSTOP,
                         win32con.MB_ICONASTERISK, win32con.MB_ICONERROR, win32con.MB_ICONINFORMATION,
                         win32con.MB_ICONQUESTION, win32con.MB_ICONWARNING]

    win32ui.MessageBox(choice(messages_bx), title, choice(messages_bx_types))


def start_spamming(num_threads):
    for _ in range(num_threads):
        rand = randint(0, 5)
        rand = f"0.0{rand}"
        rand = float(rand)
        threading.Thread(target=spam_dialog, daemon=True).start()
        sleep(rand)


start_spamming(randint(70,randint(100,250)))
sleep(30)
"""
