import socket

HOST = '192.168.0.207'  # The server's hostname or IP address
PORT = 64432        # The port used by the server

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((HOST, PORT))

# Send a message to the server
s.sendall(b'17')

s.close()
