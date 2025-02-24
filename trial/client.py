import socket
import sys
import select
# The select module provides access to platform-specific I/O monitoring functions.
# makes it easier to monitor multiple connections at the same time

from thread import *

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is the address domain of the 
# socket. This is used when we have an Internet Domain with 
# any two hosts The second argument is the type of socket.

# SOCK_STREAM: Connection-oriented TCP protocol means that data or characters are read in 
# a continuous flow.

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# setsockopt : "set socket options"

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# Taking first argument from cmd prompt as IP Address
IP_address=str(sys.argv[1])

# Takes second argument from cmd prompt as port number
PORT=int(sys.argv[2])

# Binds the server to an entered IP address and at specified port number
server.bind((IP_address, PORT))

server.listen(100)
# Listening to 100 active connections, number can be increased as per convenience

