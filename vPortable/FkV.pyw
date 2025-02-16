"""import os
import time
import random
import subprocess
import signal

# Lista dos scripts a serem executados
scripts = [
    "python Effects/BwHell.pyw",
    "python Effects/CursorFollow.pyw",
    "python Effects/Invert.pyw",
    "python Effects/RainbowHell.pyw",
    "python Effects/RandomErrors.pyw",
    "python Effects/Rectangles.pyw",
    "python Effects/Tunnel.pyw",
    "python Effects/Void.pyw",
    "python Effects/InvertScreen.pyw"
]

# Lista para armazenar os processos ativos
active_processes = []

# Função para executar o script de forma assíncrona
def run_script(script):
    # Lança o script e retorna o processo
    process = subprocess.Popen(script, shell=True)
    active_processes.append(process)  # Adiciona o processo à lista

    # Se houver mais de 5 processos ativos, termina o mais antigo
    if len(active_processes) > 5:
        # Remove o processo mais antigo da lista
        old_process = active_processes.pop(0)
        # Usa os.kill para tentar terminar o processo mais antigo
        try:
            os.kill(old_process.pid, signal.SIGTERM)  # SIGTERM termina o processo
            print(f"Processo {old_process.pid} terminado.")
        except ProcessLookupError:
            print(f"Processo {old_process.pid} não encontrado.")
        except PermissionError:
            print(f"Permissões insuficientes para terminar o processo {old_process.pid}.")

# Tocar Musica de Fundo
run_script("python Effects/audio.pyw")
# Loop para executar os scripts de forma indefinida
while True:
    # Escolher um script aleatório da lista
    script = random.choice(scripts)

    # Executar o script em paralelo
    run_script(script)
    run_script("python Effects/MoveWindows.pyw")
    run_script("python Effects/Listenner.pyw")
    run_script("python Effects/InvertScreen.pyw")


    # Aguardar um tempo aleatório entre 2 e 4 segundos
    wait_time = random.randint(2, 4)
    print(f"Aguardando {wait_time} segundos antes de executar o próximo script.")
    time.sleep(wait_time)
"""
import subprocess, os
from datetime import datetime, timedelta
import time
import random
from random import shuffle

#####################################################
#    Verifica o tempo desde a primeira execução     #
#####################################################

home_user = os.environ['USERPROFILE']
script_path = os.path.join(home_user, 'Portable', 'script_info.txt')
python_venv = f"{home_user}\\Portable\\venv\\Scripts\\python.exe"
# Armazena a data de execução
try:
    with open(script_path, 'r') as f:
        execution_date_str = f.read().strip()
        execution_date = datetime.fromisoformat(execution_date_str)
except FileNotFoundError:
    execution_date = datetime.now()
    with open(script_path, 'w') as f:
        f.write(execution_date.isoformat())

# Verifica se passaram 5 dias
if datetime.now() - execution_date > timedelta(days=3):
    subprocess.Popen(rf"python {home_user}\\Portable\\remove.py", shell=True)
else:
#####################################################

    # Lista dos scripts a serem executados
    scripts = [
        f"{python_venv} Effects/BwHell.pyw",
        f"{python_venv} Effects/CursorFollow.pyw",
        f"{python_venv} Effects/Invert.pyw",
        f"{python_venv} Effects/RainbowHell.pyw",
        f"{python_venv} Effects/RandomErrors.pyw",
        f"{python_venv} Effects/Rectangles.pyw",
        f"{python_venv} Effects/Tunnel.pyw",
        f"{python_venv} Effects/Void.pyw",
        f"{python_venv} Effects/InvertScreen.pyw",
        f"{python_venv} Effects/MoveCursor.pyw"
    ]

    # Função para executar o script de forma assíncrona
    def run_script(script):

        subprocess.Popen(script, shell=True)

    # Executa o script audio.pyw em paralelo
    subprocess.Popen(f"{python_venv} Effects/audio.pyw", shell=True)
    # Executa Em paralelo
    run_script(f"{python_venv} Effects/MoveWindows.pyw")
    run_script(f"{python_venv} Effects/Listenner.pyw")
    run_script(f"{python_venv} Effects/InvertScreen.pyw")
    run_script(f"{python_venv} Effects/DialogBoxes.pyw")

    count = 0
    # Loop para executar os scripts de forma indefinida
    shuffle(scripts)
    while count <= 9:
        # Escolher um script aleatório da lista
        #script = random.choice(scripts)

        # Executar o script em paralelo
        run_script(scripts[count])


        # Aguardar um tempo aleatório entre 2 e 4 segundos
        wait_time = random.randint(2, 4)
        print(f"Aguardando {wait_time} segundos antes de executar o próximo script.")
        time.sleep(wait_time)
        count+=1
        if count == 9:
            time.sleep(65)
            run_script(f"{python_venv} Effects/BadApple.pyw")
