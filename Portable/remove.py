import os
import subprocess
import shutil
import time
import psutil

# Inicia a contagem do tempo
start_time = time.time()

USER_PROFILE = os.environ.get("USERPROFILE")
PYTHON_ROAMING_PATH = os.path.join(USER_PROFILE, "AppData", "Roaming", "Python")
PYTHON_PROGRAM_FILES_PATH = "C:\\Program Files\\Python*"
CURRENT_DIR = os.getcwd()
PORTABLE_DEST = os.path.join(USER_PROFILE, "Portable")


def find_python():
    """Tenta encontrar o Python instalado."""
    try:
        python_exe = subprocess.run(["where", "python"], capture_output=True, text=True, check=True).stdout.strip()
        if python_exe:
            return python_exe.split("\n")[0]  # Pega o primeiro caminho encontrado
    except subprocess.CalledProcessError:
        pass

    print("Nenhuma versão do Python encontrada.")
    return None

def uninstall_chry(Dest):
    for process in psutil.process_iter(attrs=['pid','name']):
        if process.info['name'].lower() == "fkv.exe":
            psutil.Process(process.info['pid']).terminate()
    if os.path.exists(Dest):
        shutil.rmtree(Dest)
        print(f"{Dest} removido com sucesso.")
    else:
        print(f"Erro: {Dest} não encontrado.")

def main():
    python_exe = find_python()
    uninstall_chry(PORTABLE_DEST)
    if not python_exe:
        return
    # Finaliza a contagem do tempo
    end_time = time.time()

    # Calcula e imprime o tempo decorrido
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time:.4f} segundos")

if __name__ == "__main__":
    main()
