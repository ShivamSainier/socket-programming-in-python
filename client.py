import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
while True:
    full_msg=""
    new_msg=True
    while True:
        msg=s.recv(1024)
        if new_msg:
            print(f"new_msg length+{msg[:10]}")
            msglength=int(msg[:10])
            new_msg=False
        full_msg=full_msg+msg.decode("utf-8")
        if len(full_msg)-10==msglength:
            print("full msg recvd")
            new_msg=True
            full_msg=""
            print(full_msg)

