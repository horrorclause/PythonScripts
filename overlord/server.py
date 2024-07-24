#!/usr/bin/bash

# Simple TCP server

import socket

# creates a new socket object using IPv4 addressing (socket.AF_INET) and TCP protocol (socket.SOCK_STREAM).
# This socket will be used by the server to listen for incoming connections from clients.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempts to fetch the host's IP address, and set the port on which the server will listen
host = socket.gethostbyname()
port = 444

# Binds (associates) the server socket (serverSocket) with the specified host IP address and port number.
serverSocket.bind((host, port))

# Specify number of simultaneous connections to listen for
serverSocket.listen(3)

while True:
    
    # Blocks and waits until a client connects to the server. 
    # When a connection is received, it returns a new socket (clientSocket) representing the connection, 
    # and the address (address) tuple from which the client is connecting.
    clientSocket, address = serverSocket.accept()
    
    # Prints message when a connection is received to the server
    print(f"Connection received from {str(address)}")
    
    # Message for the client, and sending it when they connect to the server
    message = "Thank you for connecting to the server \r\n"
    clientSocket.send(message)
    
    # Closes the client connection
    clientSocket.close()
    
    