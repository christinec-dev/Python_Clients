## TCP Client
import socket

target_host = "www.google.com"
target_port = 80

# creates a socket object
# AF_INET = indicates we’ll use a standard IPv4 address
# SOCK_STREAM = indicates that this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to client
client.connect((target_host, target_port))

# sends data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receives data
response = client.recv(4096)

print(response.decode())
client.close()