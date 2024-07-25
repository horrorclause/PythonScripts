#!/usr/bin/python3

# Simple TCP client script

import socket

# Creates new socket object for client
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# We must specify the server IP to connect to
host = socket.gethostname()
port = 444

clientSocket.connect((host, port))

# Max amount of data allowed transmitted
message = clientSocket.recv(1024)

# Close the socket
clientSocket.close()

# Will decode and print the received message from the server
print(message.decode('ascii'))
