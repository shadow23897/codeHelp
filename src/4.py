import os
import ctypes
import sys

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
    print("\033[91m════════════════════════════════════════════════════════════════════════════\033[0m")
    print("\033[91m  https://github.com/shadow23897/codeHelp/\n https://discord.gg/codehelp \033[0m")
    print("\033[91m════════════════════════════════════════════════════════════════════════════\033[0m")
    print("\033[0m")

def activer_dns_adguard():
    os.system("cls" if os.name == "nt" else "clear")
    print("Activation du bloqueur de pub en cours...")

    if os.name == "nt":
        os.system('netsh interface ipv4 set dns name="Wi-Fi" static dns.adguard.com')  # Windows
    else:
        os.system('nmcli con mod "Wired connection 1" ipv4.dns "dns.adguard.com"')  # Linux

    print("✅ Bloqueur de pub activé avec AdGuard DNS.")

def main():
    banner()
    choix = input("Voulez-vous activer le bloqueur de pub ? (o/n) : ").strip().lower()

    if choix == "o":
        activer_dns_adguard()
    elif choix == "n":
        print("❌ Bloqueur de pub non activé.")
    else:
        print("⚠️ Entrée invalide. Réessayez.")

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


