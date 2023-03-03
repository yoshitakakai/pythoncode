import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"{client_address}: {message.decode()}")
        except:
            break
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8080))
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

start_server()