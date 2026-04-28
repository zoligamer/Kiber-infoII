import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_add=("127.0.0.1",23456)
s.sendto("hello udp".encode(),server_add)
data, _ = s.recvfrom(1024)
print("server-response",data.decode())
s.close()