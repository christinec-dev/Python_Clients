import socket
import threading

IP = "0.0.0.0"
PORT = 9998

def main():
    # We pass in the IP address and port we want the server to listen on
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # We tell the server to start listening 2, with a maximum back-log of connections set to 5
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP} {PORT}')

    # When a client connects 3, we receive the client socket in the client variable and the remote connection detailsin the address variable
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # We then start the thread to handle the client connection
        client_handler.start() 

    # We then sends a simple mes-sage back to the client
    def handle_client(client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode("utf-8")}')

    if __name__ == '__main__':
        main()
