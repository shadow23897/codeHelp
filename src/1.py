import os
import platform
import psutil
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
    print("\033[91m  https://github.com/shadow23897/codeHelp/\n https://discord.gg/codehelp\033[0m")
    print("\033[91m════════════════════════════════════════════════════════════════════════════\033[0m")

def system_info():
    print("\033[91m")
    print(f"System: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

    mem = psutil.virtual_memory()
    print(f"Total RAM: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Free RAM: {mem.available / (1024 ** 3):.2f} GB")

    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} physical cores, {psutil.cpu_count(logical=True)} logical cores")

    print("\nDisk Usage:")
    for disk in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(disk.mountpoint)
            print(f"  {disk.device} - {disk.fstype} - {usage.percent}% used")
        except PermissionError:
            print(f"  {disk.device} - {disk.fstype} - Permission denied")
    print("\033[0m")

def menu():
    banner()
    system_info()
    input("\033[91mVeuillez appuyer sur une touche pour continuer...\033[0m")
    
    
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
    menu()

