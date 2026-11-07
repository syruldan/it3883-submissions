# Program Name: Assignment4A.py
# Course: IT3883/Section W01
# Student Name: Arvin Van
# Assignment Number: Lab 4
# Due Date: 11/06/2026
# Purpose:
# This program prompts the user to enter a string, sends the string
# to Program B through a socket connection, waits for a response,
# and displays the received response on the screen.
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
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Program B
client_socket.connect((HOST, PORT))

# Get input from the user
message = input("Enter a string: ")

# Send the string to Program B
client_socket.send(message.encode())

# Receive the returned uppercase string
response = client_socket.recv(1024).decode()

# Display the response
print("Received from Program B:", response)

# Close the connection
client_socket.close()
