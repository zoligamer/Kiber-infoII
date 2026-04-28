import socket

HOST,PORT = '0.0.0.0',23456
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
print(f"UDP szerver {HOST}:{PORT}-on vár")
while True:
    data, addr = s.recvfrom(1024)
    msg=data.decode()
    print(f"Kaptam {addr}-tól :{msg}")
    s.sendto("üzenetet kaptam!".encode(),addr)