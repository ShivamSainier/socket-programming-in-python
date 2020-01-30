import socket

s=socket.socket()
print("socket genrate successfully")
s.bind(("localhost",999))
s.listen(3)
while True:
    c,add=s.accept()
    name=c.recv(1024).decode()
    print(f"connected with address {add}",name)
    c.send(bytes("welcome to my home","utf-8"))
    c.close()
