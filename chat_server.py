import socket
import threading
import os

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                if message.startswith("file:"):
                    filename = message.split(":")[1]
                    file_size = int(message.split(":")[2])
                    file_data = client_socket.recv(file_size)
                    with open(filename, "wb") as f:
                        f.write(file_data)
                    print(f"[{addr}] File '{filename}' received.")
                    client_socket.send("File received".encode("utf-8"))
                elif message == "list_files":
                    files = "\n".join(os.listdir())
                    client_socket.send(files.encode("utf-8"))
                else:
                    print(f"[{addr}] {message}")
                    client_socket.send("Message received".encode("utf-8"))
        except:
            print(f"[CONNECTION CLOSED] {addr} closed the connection.")
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen(5)
    print("[SERVER STARTED] Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
