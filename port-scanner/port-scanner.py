#Ask the user for target IP
#Scan a list of ports (e.g., 24, 18, 90)
#Try to connect to each port
#Report wether each port is opened or closed

import ipaddress
import socket

while True:
    User_IP = input("Please insert a valid IP address: ")
    
    try:
        ip = ipaddress.ip_address(User_IP)
        print("Valid IP:", ip)
        break
    except ValueError:
        print("Invalid IP address format.")

results = []
port_range = range(20, 1025)

for port in port_range:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Wait max 1 second for a response

    result = sock.connect_ex((str(ip), port))  # Try to connect to the IP and port

    if result == 0:
        print(f"Port {port} is OPEN")
        results.append((port, "open"))
    else:
        print(f"Port {port} is CLOSED")
        results.append((port, "closed"))

    sock.close()
