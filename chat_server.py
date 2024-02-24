# Imports
import socket
import threading
import os

# Start the server

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen(5)
    print("[SERVER STARTED] Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

# Function to handle each client as they connect
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            # Try to store the message
            message = client_socket.recv(1024).decode("utf-8")
            # If there is a message that was sent
            if message:
                # Check for three different types of messages
                # 1 will signify that there is a File: being sent
                # 2 will list all files that have been sent
                # 3 will be a regular message

                # 1 keyword will be file:
                if message.startswith("file:"):
                    # Get the files data
                    filename = message.split(":")[1]
                    file_size = int(message.split(":")[2])
                    file_data = client_socket.recv(file_size)

                    # Open a file with the filename specified and put the data recieved into it
                    with open(filename, "wb") as f:
                        f.write(file_data)

                    # Let the sender and reciever know that the file went through
                    print(f"[{addr}] File '{filename}' received.")
                    client_socket.send("File received".encode("utf-8"))

                # 2 keyword list_files
                elif message == "list_files":
                    files = "\n".join(os.listdir())
                    client_socket.send(files.encode("utf-8"))

                # 3 Just a regular message will be sent
                else:
                    print(f"[{addr}] {message}")
                    client_socket.send("Message received".encode("utf-8"))
        # exception to catch if the connection was lost and break the loop
        except:
            print(f"[CONNECTION CLOSED] {addr} closed the connection.")
            break

    client_socket.close()

start_server()
