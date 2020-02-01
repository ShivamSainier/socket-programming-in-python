import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
while True:
    conn, address=s.accept()
    print(f"connection with {address} is establish")
    msg="welcome to the house"
    full_msg=(f"{len(msg}:<10")
    conn.send(bytes(full_msg,"utf-8"))
    conn.close()
