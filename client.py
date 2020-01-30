import socket

c=socket.socket()

print("socket creted")

c.connect(("localhost",999))
name=input()
c.send(bytes(name,"utf-8"))

print(c.recv(1024).decode())
