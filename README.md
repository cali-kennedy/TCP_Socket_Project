# TCP Socket Project

This project demonstrates a basic TCP client-server model using Python sockets. The server listens for incoming client connections, receives messages, and sends responses back. This setup is commonly used to understand network communication and is foundational in developing networked applications.

## Files
- **TCPserver.py**: The server script that waits for client connections and responds to incoming messages.
- **TCPclient.py**: The client script that connects to the server, sends a message, and receives a response.

## Requirements
- **Python 3.x**

## How to Run
1. **Start the Server**:
   - Open a terminal in the directory containing `TCPserver.py`.
   - Run the server script:
     ```bash
     python3 TCPserver.py
     ```

2. **Run the Client**:
   - Open a new terminal in the same directory.
   - Run the client script:
     ```bash
     python3 TCPclient.py
     ```

3. **Send Messages**:
   - The client will prompt you to enter a message.
   - After entering a message, it will be sent to the server, and the server’s response will be displayed.

## Configuration
The client and server communicate on `localhost` and port `12000` by default. You can change the server IP and port in the code:
- **TCPserver.py**:
  ```python
  serverPort = 12000
