import os
import shutil
import psutil
import subprocess
import ctypes
import time
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")
    print("░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓███████▓▒░")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░")
    print(" ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░")
    print("\033[91m══════════════════════════════════════════════════════════\033[0m")
    print("\033[91m  https://github.com/shadow23897/codeHelp/\n https://discord.gg/codehelp\033[0m")
    print("\033[91m══════════════════════════════════════════════════════════\033[0m")

def close_unnecessary_programs():
    processes_to_kill = ["OneDrive.exe", "Skype.exe", "Discord.exe", "Steam.exe", "EpicGamesLauncher.exe"]
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if proc.info['name'] in processes_to_kill:
                print(f"Fermeture de {proc.info['name']}...")
                psutil.Process(proc.info['pid']).terminate()
        except psutil.NoSuchProcess:
            pass

def empty_recycle_bin():
    print("Vidage de la corbeille...")
    os.system("PowerShell.exe -Command Clear-RecycleBin -Force")

def delete_temp_files():
    temp_folders = [os.environ['TEMP'], os.environ['TMP'], "C:\\Windows\\Temp"]
    for folder in temp_folders:
        try:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            print(f"Fichiers temporaires supprimés dans {folder}")
        except Exception as e:
            print(f"Erreur lors du nettoyage de {folder}: {e}")

def clear_ram():
    print("Nettoyage de la RAM...")
    os.system("PowerShell.exe -Command Clear-PhysicalMemoryCache")

def flush_dns():
    print("Vidage du cache DNS...")
    os.system("ipconfig /flushdns")

def clean_windows_update():
    print("Suppression des fichiers inutiles de Windows Update...")
    os.system("cmd.exe /c cleanmgr /sagerun:1")

def main():
    banner()
    if not is_admin():
        print("❌ Ce script doit être exécuté en mode administrateur !")
        input("\nAppuyez sur une touche pour fermer cette fenêtre...")
        if os.name == 'nt':
            try:
                hwnd = ctypes.windll.kernel32.GetConsoleWindow()
                if hwnd:
                    ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
            except Exception as e:
                print("Erreur lors de la fermeture de la fenêtre :", e)
        else:
            sys.exit()
        return

    print("\n🔹 Nettoyage du PC en cours...\n")
    close_unnecessary_programs()
    empty_recycle_bin()
    delete_temp_files()
    clear_ram()
    flush_dns()
    clean_windows_update()
    print("\n✅ Nettoyage terminé ! Votre PC est optimisé.\n")
    input("\nAppuyez sur une touche pour continuer...")
    if os.name == 'nt':
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                
                ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
        except Exception as e:
            print("Erreur lors de la fermeture de la fenêtre :", e)
    else:
        sys.exit()

if __name__ == "__main__":
    main()



