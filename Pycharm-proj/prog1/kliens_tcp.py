import socket
HOST="127.0.0.1"
PORT=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
msg="Message"
s.sendall(msg.encode())
data=s.recv(1024)
print(f"Received {data}")
s.close()