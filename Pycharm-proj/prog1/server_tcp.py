import socket
HOST='0.0.0.0'
PORT=8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
print('[*] Server Listening{HOST}:{PORT}'.format(HOST=HOST,PORT=PORT))
conn,addr=s.accept()
print(f'[*] Connected {addr}')
data=conn.recv(1024)
print(f'[*] Received {data}')
eredmeny="Message recieved"
conn.sendall(eredmeny.encode())
conn.close()
s.close()