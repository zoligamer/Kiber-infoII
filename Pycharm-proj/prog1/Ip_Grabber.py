import socket

from scapy.layers.inet import IP

domain = str(input("Enter your domain: "))
ip=socket.gethostbyname(domain)
print(f"Host address: IP:{ip}, DNS:{domain}")