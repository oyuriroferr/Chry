import os
import subprocess
import glob
import time

# Inicia a contagem do tempo // Fechamento do Serviço 3
start_time = time.time()

USER_PROFILE = os.environ.get("USERPROFILE")
PYTHON_ROAMING_PATH = os.path.join(USER_PROFILE, "AppData", "Roaming", "Python")
PYTHON_PROGRAM_FILES_PATH = "C:\\Program Files\\Python*"
CURRENT_DIR = os.getcwd()
PORTABLE_SOURCE = os.path.join(CURRENT_DIR, r"vPortable")
PORTABLE_DEST = os.path.join(USER_PROFILE, "Portable")
VENV_PATH = os.path.join(PORTABLE_DEST, "venv")
ATALHO_SCRIPT = os.path.join(PORTABLE_DEST, "atalho.py")
FKV_SCRIPT = os.path.join(PORTABLE_DEST, "FkV.pyw")
python_path = open("python_path.txt","r")
python_path = python_path.readlines()
"""
NAO COMPATIVEL COM VERSOES DIFERENTES DE 3.(10,13,12,11)

def find_python():
    ### Tenta encontrar o Python instalado. ###
    try:
        python_exe = subprocess.run(["where", "python"], capture_output=True, text=True, check=True).stdout.strip()
        if python_exe:
            return python_exe.split("\n")[0]  # Pega o primeiro caminho encontrado
    except subprocess.CalledProcessError:
        pass

    roaming_python = glob.glob(os.path.join(PYTHON_ROAMING_PATH, "Python*", "python.exe"))
    if roaming_python:
        return roaming_python[0]

    program_files_python = glob.glob(os.path.join(PYTHON_PROGRAM_FILES_PATH, "python.exe"))
    if program_files_python:
        return program_files_python[0]

    print("Nenhuma versão do Python encontrada.")
    return None
"""

def create_venv(python_exe):
    print("\n\033[0;35m+ PYTHON (InitV)")
    """Cria um ambiente virtual dentro da pasta Portable."""
    print(f"Python Global (Criando Venv): {python_exe}")
    if not os.path.exists(VENV_PATH):
        print(f"Criando ambiente virtual em {VENV_PATH}...")
        subprocess.run([python_exe, "-m", "venv", VENV_PATH], check=True)
    else:
        print("Ambiente virtual já existe.")

def install_packages():
    azul = "\033[1;34m"
    reset = "\033[0m"
    ciano_bold = "\033[1;36m"
    verde_claro = "\033[91m"

    print("\n\033[0;36m- PYTHON INSTALL (VENV)\033[0m")
    
    # Instala os pacotes necessários no ambiente virtual.
    venv_python = os.path.join("C:\\Users\\teste\\Portable\\venv", "Scripts", "python.exe")
    print(f"\033[0;36m- Python Venv (Instalando pacotes na Venv): {venv_python}\033[0m")

    try:
        print(f"{reset}{azul}|")

        process = subprocess.Popen(
            [venv_python, "-m", "pip", "install", "pywin32", "pynput", "pyautogui", "psutil", "ffpyplayer", "pygame"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate()  # Captura toda a saída ao invés de iterar
        output_lines = stdout.strip().split("\n")
        error_lines = stderr.strip().split("\n")

        for i, line in enumerate(output_lines):
            print(f"{azul}|--{ciano_bold}>{reset}     {verde_claro}{line}{reset}") 
            if i < len(output_lines) - 1:  # Evita imprimir "|" na última linha
                print(f"{azul}|")

        for i, line in enumerate(error_lines):
            if line.strip():  # Evita imprimir erros vazios
                print(f"{azul}|--{ciano_bold}>{reset}     \033[91m{line}{reset}")
            if i < len(error_lines) - 1:
                print(f"{azul}|")

    except subprocess.CalledProcessError as e:
        print(f"\033[91mErro ao instalar pacotes: {e}{reset}")

def copy_portable():
    print("\n\033[0;35m+ PYTHON (InitV)")
    """Copia a pasta PORTABLE para o diretório do usuário usando xcopy."""
    if os.path.exists(PORTABLE_SOURCE):
        cmd = ["cmd", "/c", "xcopy", PORTABLE_SOURCE, PORTABLE_DEST, "/E", "/I", "/Y"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("Pasta PORTABLE copiada com sucesso.")
        else:
            print(f"Erro ao copiar a pasta PORTABLE: {result.stderr}")
    else:
        print("Erro: A pasta PORTABLE não foi encontrada.")


def execute_script():
    print("\n\033[0;35m+ PYTHON (InitV)")
    """Executa o script atalho.py dentro do ambiente virtual."""
    venv_python = os.path.join(VENV_PATH, "Scripts", "python.exe")
    print(f"Python Venv (Executando atalho.py com a Venv): {venv_python}")

    if os.path.exists(ATALHO_SCRIPT):
        result = subprocess.run([venv_python, ATALHO_SCRIPT], capture_output=True, text=True)
        if result.stdout.strip():
            print(result.stdout.strip())
            
        if result.stderr.strip():
            print(result.stderr.strip())
        
        
    else:
        print("Erro: atalho.py não encontrado.")


def cleanup():
    print("\n\033[0;35m+ PYTHON (InitV)")
    """Remove os scripts atalho.py e FkV.pyw."""
    for script in [ATALHO_SCRIPT, FKV_SCRIPT]:
        if os.path.exists(script):
            os.remove(script)
            print(f"{script} removido com sucesso.")
        else:
            print(f"Erro: {script} não encontrado.")


def main():
    python_exe = str(python_path[0]).strip()
    copy_portable()
    with open("vPortable\\python.txt","w") as file:
        file.write(python_exe)
        file.close()
    """if not python_exe:
                    return"""
    create_venv(python_exe)
    install_packages()
    execute_script()
    cleanup()

    # Finaliza a contagem do tempo
    end_time = time.time()

    # Calcula e imprime o tempo decorrido
    execution_time = end_time - start_time
    print(f"\n\033[4;32mTempo de execucao: {execution_time:.4f} segundos.\033[0m")


if __name__ == "__main__":
    main()
