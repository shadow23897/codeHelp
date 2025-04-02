import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import os
import ctypes
import sys

init(autoreset=True)

def banner():
    print("\033c", end="")  
    print(Fore.RED + "░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░")
    print(Fore.RED + "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░")
    print(Fore.RED + "░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░")
    print(Fore.RED + "░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓███████▓▒░")
    print(Fore.RED + "░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░")
    print(Fore.RED + "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░")
    print(Fore.RED + " ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░")
    print(Fore.RED + "════════════════════════════════════════════════════════════════════════════")
    print(Fore.RED + "  https://github.com/shadow23897/codeHelp/ \n  https://discord.gg/codehelp")
    print(Fore.RED + "════════════════════════════════════════════════════════════════════════════")

banner()

API_KEY = "AIzaSyDrWcK42i2Yl0PZgFQEYCuQqVgpv0s-0HM"
API_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

def check_url(url):
    payload = {
        "client": {
            "clientId": "python-tool",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    response = requests.post(f"{API_URL}?key={API_KEY}", json=payload)
    data = response.json()

    if "matches" in data:
        print(f"⚠️ DANGER ! L'URL {url} est potentiellement malveillante.")
    else:
        print(f"✅ L'URL {url} semble sûre.")

if __name__ == "__main__":
    url = input("🔍 Entre l'URL à vérifier : ")
    check_url(url)

    input("\n🔄 Appuyez sur une touche pour continuer...")

   
    if os.name == 'nt':
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
        except Exception as e:
            print("Erreur lors de la fermeture de la fenêtre :", e)
    else:
        sys.exit()
