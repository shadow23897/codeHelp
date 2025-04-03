import requests
from bs4 import BeautifulSoup  
from colorama import init, Fore
import os
import sys


init(autoreset=True)

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

def get_ip_info(ip):
    
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return data
    except Exception as e:
        print(Fore.RED + f"Erreur lors de la récupération des informations : {e}")
        return None

def main():
    banner()
    ip = input(Fore.YELLOW + "Entrez une adresse IP à vérifier : " + Fore.RESET)
    data = get_ip_info(ip)
    if data:
        if data.get("status") == "success":
            print(Fore.GREEN + "\nInformations sur l'IP:\n")
            for key, value in data.items():
                print(f"{Fore.CYAN}{key}: {Fore.WHITE}{value}")
        else:
            print(Fore.RED + f"\nErreur: {data.get('message', 'Erreur inconnue')}")
    else:
        print(Fore.RED + "\nAucune donnée récupérée.")
    
    input("\nAppuyez sur une touche pour continuer...")
    
    if os.name == 'nt':
        try:
            import ctypes
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                
                ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
        except Exception as e:
            print("Erreur lors de la fermeture de la fenêtre :", e)
    else:
        sys.exit()

if __name__ == "__main__":
    main()
