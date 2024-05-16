"""
This script defines the server side of a multi-client chat app. 
"""

import socket  # Importing the socket module for network communication
import threading  # Importing threading module for concurrent execution

# Dictionary to store client names and sockets
clients = {}

def handle_client(client_socket, client_address, client_name):
    try:
        # Continuous loop to handle client communication
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode("utf-8")
            
            # Check if message is empty
            if not message:
                break
            
            # Check if message is a direct message
            if message.startswith('@'):
                try:
                    # Split message into recipient name and message body
                    recipient_name, message_body = message[1:].split(':', 1)
                except ValueError:
                    # Send error message if message format is invalid
                    client_socket.send("Error: Invalid message format for direct message.".encode("utf-8"))
                    continue
                
                # Look up recipient's socket in clients dictionary
                recipient_socket = clients.get(recipient_name)
                
                # If recipient found, send message to recipient
                if recipient_socket:
                    sender_name = clients[client_socket]
                    recipient_socket.send(f"{sender_name}: {message_body}".encode("utf-8"))
                    client_socket.send(f"To {recipient_name}: {message_body}".encode("utf-8"))
                else:
                    # If recipient not found, send error message to sender
                    client_socket.send(f"Error: User {recipient_name} not found.".encode("utf-8"))
            
            # If message is not a direct message, broadcast it to all clients
            else:
                sender_name = clients[client_socket]
                for socket, name in clients.items():
                    if socket != client_socket:
                        socket.send(f"{sender_name}: {message}".encode("utf-8"))
    
    # Handle connection reset by client
    except ConnectionResetError:
        print(f"Connection with {client_name} ({client_address}) reset by client.")
    
    # Handle other exceptions
    except Exception as e:
        print(f"Error handling message from {client_name}: {e}")
    
    # Clean up client socket and remove from clients dictionary
    finally:
        del clients[client_socket]
        client_socket.close()
        print(f"Connection with {client_name} ({client_address}) closed.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a TCP socket
    server.bind(('localhost', 12345))  # Binding the socket to localhost and port 12345
    server.listen(5)  # Listening for incoming connections with a backlog of 5

    print("Server started. Waiting for connections...")

    while True:
        client_socket, client_address = server.accept()  # Accepting incoming connection

        # Ask the client for their name
        client_socket.send("Enter your name: ".encode("utf-8"))  # Sending prompt to enter name
        client_name = client_socket.recv(1024).decode("utf-8")  # Receiving client name

        clients[client_socket] = client_name  # Storing client name and socket in dictionary
        print(f"{client_name} connected from {client_address}")  # Printing client details

        # Starting a new thread to handle client communication
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_name))
        client_thread.start()  # Starting the client thread

if __name__ == "__main__":
    main()  # Calling the main function when script is executed


