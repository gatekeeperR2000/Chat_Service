import socket
import os

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    while True:
        message = input("Enter message ('list_files' for file list, or file path prefixed with 'file:'): ")
        if message == "list_files":
            client_socket.send(message.encode("utf-8"))
            file_list = client_socket.recv(1024).decode("utf-8")
            print("[SERVER FILE LIST]:\n", file_list)
        elif message.startswith("file:"):
            filename = message.split(":")[1]
            file_size = os.path.getsize(filename)
            client_socket.send(f"file:{filename}:{file_size}".encode("utf-8"))
            with open(filename, "rb") as f:
                file_data = f.read()
            client_socket.send(file_data)
            print("File sent.")
            response = client_socket.recv(1024).decode("utf-8")
            print("[SERVER]:", response)
        else:
            client_socket.send(message.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8")
            print("[SERVER]:", response)

if __name__ == "__main__":
    start_client()
