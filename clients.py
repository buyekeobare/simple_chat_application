"""
This script defines the chat application that connects to a server, 
sends and receives messages, and handles errors.
"""

import socket  # Importing the socket module for network communication
import threading  # Importing threading module for concurrent execution

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                # If the message is empty, it means the server closed the connection
                print("Server closed the connection.")
                break
            # Print the received message
            print(message)
        except ConnectionResetError:
            # Handle connection reset error
            print("Connection with the server was reset.")
            break
        except Exception as e:
            # Handle other exceptions that may occur during message receiving
            print(f"Error receiving message: {e}")
            break

def main():
    # Creating a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connecting to the server
        client.connect(('localhost', 12345))
    except ConnectionRefusedError:
        # Handle connection refused error
        print("Failed to connect to the server. Please make sure the server is running.")
        return
    except Exception as e:
        # Handle other connection errors
        print(f"Error connecting to the server: {e}")
        return

    while True:
        # Prompt the user to enter their name
        client_name = input("Enter your name: ")
        # Send the client name to the server
        client.send(client_name.encode("utf-8"))
        # Receive response from the server
        response = client.recv(1024).decode("utf-8")
        if response.startswith("Error"):
            # If the response indicates an error, print the error message
            print(response)
        else:
            # If the connection is successful, print a success message
            print("Connected to server. You can start sending messages.")
            break

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    try:
        # Main thread to send messages to the server
        while True:
            message = input()  # Input message from the user
            client.send(message.encode("utf-8"))  # Send the message to the server
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl+C) to exit the client
        print("Client exiting...")
    except Exception as e:
        # Handle other exceptions that may occur during message sending
        print(f"Error sending message: {e}")
    finally:
        # Close the client socket
        client.close()

if __name__ == "__main__":
    main()


