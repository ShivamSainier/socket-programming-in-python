import socket
import sys

# create a socket function
try:
    host=""
    port=999
    s=socket.socket()   # to create a socket
except socket.error as e:
    print(f"socket creation error {e}")

