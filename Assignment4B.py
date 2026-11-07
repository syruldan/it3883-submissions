# Program Name: Assignment4B.py
# Course: IT3883/Section W01
# Student Name: Arvin Van
# Assignment Number: Lab 4
# Due Date: 11/06/2026
# Purpose:
# This program waits for a connection from Program A, receives
# a string, converts the string to uppercase, sends it back to
# Program A, and then closes the connection.
#
# Resources Used:
# Python Documentation - socket module
# Course lecture notes and examples

# Import the socket library
import socket

# Server information
HOST = '127.0.0.1'      # Localhost
PORT = 45000            # Port number

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print("Program B is listening for connections...")

# Accept a connection from Program A
connection, address = server_socket.accept()

print("Connected by:", address)

# Receive data from Program A
message = connection.recv(1024).decode()

# Convert the message to uppercase
uppercase_message = message.upper()

# Send the uppercase message back to Program A
connection.send(uppercase_message.encode())

# Close the connection
connection.close()

# Close the server socket
server_socket.close()