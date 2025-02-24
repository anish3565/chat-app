############# Client-Side

import socket

s=socket.socket()

# Define port on which we want to connect
port=12345

# Connect to server on local computer
s.connect(('127.0.0.1', port))

# Receive data from the server and decoding to get the string
print(s.recv(1024).decode())

# Close the connection
s.close()