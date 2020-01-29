import socket
import sys

# create a socket function
def socket():
    try:
        global host
        global port
        global s
        host=""
        port=999
        s=socket.socket()   # to create a socket
    except socket.error as e:
        print(f"socket creation error {e}")

 # create a bind function
def bind():
    try:
        global host
        global port
        global s
        print(f"binding the port {str(port)}")
        s.bind(host/port)
        s.listen(5)
    except socket.error as e:
        print(f"socket faild {e}")
        bind()







