# import socket
# import sys


# #### Socket creation 
# try:
#     s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # AF_INET : Refers to address-family ipv4
#     # SOCK_STREAM : Connection-oriented TCP protocol
#     print("Socket successffully created")
# except socket.error as err:
#     print("Socket creation failed with error %s" %(err))

# port=80

# #### Connecting socket ip to google
# try:
#     host_ip=socket.gethostbyname('www.google.com')
# except socket.gaierror: #gaierror: Exception raised for addreess-related errors by getaddressinfo() and getnameinfo()
#     print("There was an error resolving the host")
#     sys.exit()

# s.connect((host_ip, port))

# print("Socket has successfully connected to google")

# # Sendall : Used for sending data to a server to which the sockets is connected and also server can send data to the client using this function


# #### Simple Client-server connection

# ## Server methods:

# # - bind() : Binds server to a specific IP and port so it can listen to upcoming requests on that IP and port.
# # - listen() : Puts server to listening mode. Allows server to listening mode allowing server to listen to incoming connections
# # - accept() : initiates connection with client
# # - close() : Closes the connection with client




########### Simple client server program

import socket

s=socket.socket()
print("Socket successfully created")
port=12345
#  As ip is not bound to any ip to ip field and instead inputted empty string
# Allows the server to listen to request coming from outher computers on the network

s.bind(('', port)) # Allows server to listen to incoming connections from other computers as well
# s.bind(('127.0.0.1', port)) # Allows server to listen to incoming connections from local computer


print("Socket binded to %s" %(port))
# Putting socket in listening mode
s.listen(5) 
# We put the server into listening mode.5 here means that 5 connections are kept waiting if the server is busy 
# and if a 6th socket tries to connect then the connection is refused.


# A forever loop till we interrupt it or an error occurs
while True:
    c, addr = s.accept()
    print('Got connections from', addr)

    # Sending message to client: "Thank you"; Encoding to send byte type

    c.send('Thank you for connection'.encode())

    # Closing the connection with the ckinet
    c.close()

    break