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

list_of_clients=[]

def clientThread(conn, addr):

    # Sending a message to the client whose user object is conn
    conn.send("Welcome to the chatroom!")

    while True:
        try:
            message=conn.recv(2048)
            if message:
                # Prints message and address of the client that sent the message to the server terminal
                print("<" + addr[0] + ">" + message)

                # Calls broadcast function to send message to all
                message_to_send="<"+addr[0]+">"+message
                broadcast(message_to_send, conn)

            else:
                # Remove the message if its broken or have no content
                remove(conn)
        except:
            continue

"""
Broadcasting message to all clients whose object is not the same as the one sending the message
"""
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)

"""
Removing the object from the list that was created at the beginning of the program
"""
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    """
    Accepts a connection requests and stores two parameters, 
    conn which is a socket object for that user,
    and addr which contains the IP address of the client that just connected
    """
    