import os
import subprocess
import sys

def run_as_admin():

    if os.name == 'nt':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("\033[91mDemande d'exécution en mode administrateur...\033[0m")
            try:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                sys.exit()
            except:
                print("\033[91mÉchec de la demande d'administrateur.\033[0m")

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")
    print("░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░  ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓███████▓▒░  ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        ")
    print(" ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░        ")
    print("\033[91m══════════════════════════════════════════════════════════\033[0m")
    print("\033[91m  https://github.com/shadow23897/codeHelp/\033[0m")
    print("\033[91m══════════════════════════════════════════════════════════\033[0m")


def main_menu():
    banner()
    print("\033[92m[1] - System info\033[0m")
    print("\033[92m[2] - System cleaner\033[0m")
    print("\033[92m[3] - website clone\033[0m")
    print("\033[92m[4] - bloqueur de pub free\033[0m")
    print("\033[92m[5] - Quitter\033[0m")
    choix = input("\nChoisissez une option : ")

    if choix == "1":
        run_script("1.py")
    elif choix == "2":
        run_script("2.py")
    elif choix == "3":
        run_script("3.py")
    elif choix == "4":
        run_script("4.py")
    elif choix == "5":
        print("\n\033[91mFermeture du programme...\033[0m")
        exit()
    else:
        print("\033[91mOption invalide, veuillez réessayer.\033[0m")
        main_menu()

def run_script(script_name):
    script_path = os.path.join("src", script_name)
    if os.path.exists(script_path):
        if os.name == 'nt':
            subprocess.run(["powershell", "Start-Process", "python", f"-ArgumentList {script_path}", "-Verb", "RunAs"], check=True)
        else:
            subprocess.run(["python", script_path], check=True)
    else:
        print(f"\033[91mErreur : {script_name} introuvable dans src\033[0m")

if __name__ == "__main__":
    if os.name == 'nt':
        import ctypes
        run_as_admin()
    main_menu()
