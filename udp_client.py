## UDP Client
import socket

target_host = "127.0.0.1"
target_port = 9997

# creates a socket object
# AF_INET = indicates we’ll use a standard IPv4 address
# SOCK_DGRAM = indicates that this will be a UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sends data
client.sendto(b"AAABBBCCC",(target_host, target_port))

# receives data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()