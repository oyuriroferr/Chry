import os
import subprocess
import glob
import time

# Inicia a contagem do tempo
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


def find_python():
    """Tenta encontrar o Python instalado."""
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


def create_venv(python_exe):
    """Cria um ambiente virtual dentro da pasta Portable."""
    if not os.path.exists(VENV_PATH):
        print(f"Criando ambiente virtual em {VENV_PATH}...")
        subprocess.run([python_exe, "-m", "venv", VENV_PATH], check=True)
    else:
        print("Ambiente virtual já existe.")


def install_packages():
    """Instala os pacotes necessários no ambiente virtual."""
    venv_python = os.path.join(VENV_PATH, "Scripts", "python.exe")
    try:
        subprocess.run([venv_python, "-m", "pip", "install", "pywin32", "pynput", "pygame", "pyautogui","psutil","ffpyplayer"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar pacotes: {e}")


def copy_portable():
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
    """Executa o script atalho.py dentro do ambiente virtual."""
    venv_python = os.path.join(VENV_PATH, "Scripts", "python.exe")
    if os.path.exists(ATALHO_SCRIPT):
        result = subprocess.run([venv_python, ATALHO_SCRIPT], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    else:
        print("Erro: atalho.py não encontrado.")


def cleanup():
    """Remove os scripts atalho.py e FkV.pyw."""
    for script in [ATALHO_SCRIPT, FKV_SCRIPT]:
        if os.path.exists(script):
            os.remove(script)
            print(f"{script} removido com sucesso.")
        else:
            print(f"Erro: {script} não encontrado.")


def main():
    python_exe = find_python()
    copy_portable()
    with open("vPortable\\python.txt","w") as file:
        file.write(python_exe)
        file.close()
    if not python_exe:
        return
    create_venv(python_exe)
    install_packages()
    execute_script()
    cleanup()
    # Finaliza a contagem do tempo
    end_time = time.time()

    # Calcula e imprime o tempo decorrido
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time:.4f} segundos")


if __name__ == "__main__":
    main()
