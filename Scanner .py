import socket
import sys
from datetime import datetime

def start_scan():
    target = input("Enter website or IP to scan (e.g., google.com): ")
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Hostname galat hai.")
        sys.exit()

    print("-" * 50)
    print(f"Scanning: {target_ip}")
    print("-" * 50)

    ports = [21, 22, 80, 443, 8080]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: CLOSED")
        s.close()

if __name__ == "__main__":
    start_scan()