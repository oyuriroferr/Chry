import os
import win32com.client


def create_shortcut(target, shortcut_name, description=None, icon_path=None):
    # Obtém o caminho da área de trabalho
    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

    # Cria um atalho usando o Shell.Application
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)

    # Configurações do atalho
    shortcut.TargetPath = target  # Caminho do executável ou arquivo
    shortcut.WorkingDirectory = os.path.dirname(target)  # Diretório de trabalho
    shortcut.Description = description or shortcut_name  # Descrição
    if icon_path:
        shortcut.IconLocation = icon_path  # Caminho do ícone

    # Salva o atalho
    shortcut.save()
    print(f"Atalho criado: {shortcut_path}")


# Exemplo de uso
user = os.environ['USERPROFILE']
create_shortcut(
    target=rf"{user}\\Portable\\FkV.exe",  # Caminho do programa ou script
    shortcut_name="Google Chrome",
    description="Acessar a Internet",
    icon_path=rf"{user}\\Portable\\chrome.ico"  # Opcional: caminho do ícone
)
