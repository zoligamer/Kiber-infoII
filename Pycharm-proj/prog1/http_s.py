import socket
HOST, PORT = "",8001
s=socket.socket()
s.bind((HOST,PORT))
s.listen(1)
print(f"egyszeru http szerver indult porton: {PORT}")
while True:
    conn,addr=s.accept()
    req=conn.recv(1024).decode()
    print("request:",req.splitlines()[0])
    if not req: break
    response=("HTTP 200 OK")
    conn.sendall(response.encode())
    conn.close()