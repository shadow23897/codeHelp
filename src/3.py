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
    print(Fore.RED + "  https://github.com/shadow23897/codeHelp/\n https://discord.gg/codehelp")
    print(Fore.RED + "════════════════════════════════════════════════════════════════════════════")

banner()

url = input("Entrez l'URL du site : ")

if not url.startswith("http"):
    url = "http://" + url

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    html_filename = "site_code.html"
    with open(html_filename, "w", encoding="utf-8") as file:
        file.write(soup.prettify())
    print(f"Le code HTML a été sauvegardé dans {html_filename}")

    css_links = soup.find_all("link", {"rel": "stylesheet"})
    css_files = []

    for link in css_links:
        css_url = link.get("href")
        if css_url:
            if not css_url.startswith("http"):
                css_url = requests.compat.urljoin(url, css_url)
            css_files.append(css_url)

    for index, css_url in enumerate(css_files):
        try:
            css_response = requests.get(css_url, timeout=10)
            css_response.raise_for_status()
            css_filename = f"style_{index + 1}.css"
            with open(css_filename, "w", encoding="utf-8") as css_file:
                css_file.write(css_response.text)
            print(f"Le fichier CSS a été sauvegardé dans {css_filename}")
        except requests.RequestException:
            print(f"⚠ Impossible de télécharger le fichier CSS : {css_url}")

    js_files = []
    script_tags = soup.find_all("script", {"src": True})

    for script in script_tags:
        js_url = script.get("src")
        if js_url:
            if not js_url.startswith("http"):
                js_url = requests.compat.urljoin(url, js_url)
            js_files.append(js_url)

    for index, js_url in enumerate(js_files):
        try:
            js_response = requests.get(js_url, timeout=10)
            js_response.raise_for_status()
            js_filename = f"script_{index + 1}.js"
            with open(js_filename, "w", encoding="utf-8") as js_file:
                js_file.write(js_response.text)
            print(f"Le fichier JavaScript a été sauvegardé dans {js_filename}")
        except requests.RequestException:
            print(f"⚠ Impossible de télécharger le fichier JS : {js_url}")

except requests.RequestException as e:
    print(f"❌ Erreur lors de la récupération du site : {e}")


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

