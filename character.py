#!/bin/python3

import socket

host = "83.136.249.138"
port = 54104

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


server_prompt = s.recv(1024).decode()
print(server_prompt)

# Generate a dynamic response based on the prompt
response_to_send = "0"

s.sendall(response_to_send.encode())

# Receive and print the server's final response
final_response = s.recv(1024).decode()
print(f"Received final response: {final_response}")




