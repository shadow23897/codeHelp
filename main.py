import os
import subprocess
import sys
import ctypes

def run_as_admin():
    if os.name == 'nt':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("\033[91mDemande d'exécution en mode administrateur...\033[0m")
            try:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            except Exception as e:
                print("\033[91mÉchec de la demande d'administrateur.\033[0m")
                print(e)
            # Ferme immédiatement le processus d'origine pour que la fenêtre se ferme
            os._exit(0)

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")
    print("░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░  ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓███████▓▒░  ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        ")
    print(" ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░        ")
    print("\033[91m══════════════════════════════════════════════════════════\033[0m")
    print("\033[91m  https://github.com/shadow23897/codeHelp/ \n  https://discord.gg/codehelp\033[0m")
    print("\033[91m══════════════════════════════════════════════════════════\033[0m")

def main_menu():
    while True:
        banner()
        print("\033[92m[1] - System info\033[0m")
        print("\033[92m[2] - System cleaner\033[0m")
        print("\033[92m[3] - Website clone\033[0m")
        print("\033[92m[4] - Bloqueur de pub free\033[0m")
        print("\033[92m[5] - Verify link virus\033[0m")
        print("\033[92m[6] - ip lookup\033[0m")
        print("\033[92m[7] - Quitter\033[0m")
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
            run_script("5.py")
        elif choix == "6":
            run_script("6.py")
        elif choix == "7":
            print("\n\033[91mFermeture du programme...\033[0m")
            break
        else:
            print("\033[91mOption invalide, veuillez réessayer.\033[0m")

def run_script(script_name):
    script_path = os.path.join("src", script_name)
    if os.path.exists(script_path):
        if os.name == 'nt':
            subprocess.run([
                "powershell",
                "-Command",
                f"Start-Process cmd -ArgumentList '/k python \"{script_path}\"' -Verb RunAs"
            ], check=True)
        else:
            subprocess.run(["python", script_path], check=True)
    else:
        print(f"\033[91mErreur : {script_name} introuvable dans src\033[0m")

if __name__ == "__main__":
    if os.name == 'nt':
        run_as_admin()
    main_menu()


