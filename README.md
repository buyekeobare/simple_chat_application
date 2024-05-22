# Command Line ChatApp

Welcome to the **Command Line ChatApp**! This application allows users to communicate with each other in real-time via the command line interface.

## Features

- **Real-time messaging:** Users can send and receive messages instantly.
- **Username registration:** Users can register a username to identify themselves in the chat.
- **Multi-user support:** Multiple users can connect to the server and participate in the chat simultaneously.
- **Graceful shutdown:** The server can be gracefully shut down, closing all client connections cleanly.

## Installations

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
```

2. Navigate to to the project directory:

```bash
cd Cmdline_ChatApp
```

3. Install the required dependencies (if any):

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
python server.py
```

2. Start the client:

```bash
python client.py
```

3. Follow the prompts to register your username and start chatting!

## Configuration

- The server address and port can be configures in the `server.py`
- Additional configuration options may be available in the future releases.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure all tests pass.
4. Commit your changes and push them to your fork.
5. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [Apache License](LICENSE).
