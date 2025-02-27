import socket
import platform
import subprocess


Target_ip = ""
Target_port = 80
Target_port_end = 1


def ping_ip(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if response.returncode == 0:
        print(f"{ip} ist erreichbar.")
    else:
        print(f"{ip} ist nicht erreichbar.")
        exit()

print("Welcome to my Portscanner Github Mr-Catfish")
print("Have Fun!")
Target_ip = input("What is the Ip of the Target? ")

ping_ip(Target_ip)

if input("Do you want to scan multiple ports? (y/n) ") == "n":
    Target_port = int(input("Which Port do you want to scan? "))
    Target_port_end = Target_port
    print("Scanning...")
else:
    print("Ok, what port range do you want to scan?")
    Target_port = int(input("from "))
    Target_port_end = int(input("to "))
    


def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.settimeout(2)
    
    result = s.connect_ex((host, port))
    
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} closed")
    
    s.close()


while Target_port <= Target_port_end:
    scan_port(Target_ip, Target_port)
    Target_port += 1 

