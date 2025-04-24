import socket
import threading
import json
import hashlib
import secrets
from sdatabase import sDatabase

HOST = "0.0.0.0"
PORT = 5000

db = sDatabase()
clients = {}
tokens = {}
connected_users = {}

def generate_token():
    """Generate a secure random token."""
    return secrets.token_hex(16)

def handle_client(conn, addr):
    """Handle client requests."""
    global clients, tokens, connected_users
    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            request = json.loads(data)
            action = request.get("action")

            if action == "register":
                username = request.get("username")
                password = request.get("password")
                email = request.get("email")
                pin = request.get("pin")

                if db.register_user(username, password, email, pin):
                    conn.sendall(json.dumps({"status": "success", "message": "Registration successful!"}).encode())
                else:
                    conn.sendall(json.dumps({"status": "error", "message": "Registration failed. Username may already exist."}).encode())

            elif action == "login":
                username = request.get("username")
                password = request.get("password")

                if db.validate_login(username, password):
                    token = generate_token()
                    tokens[username] = token
                    connected_users[username] = conn  # adds username to list of connected users
                    conn.sendall(json.dumps({"status": "success", "message": "Login successful!", "token": token}).encode())
                else:
                    conn.sendall(json.dumps({"status": "error", "message": "Invalid username or password."}).encode())

            elif action == "account_reset":
                email = request.get("email")
                pin = request.get("pin")

                account_info = db.retrieve_account(email, pin)
                if account_info:
                    conn.sendall(json.dumps({"status": "success", "message": account_info}).encode())
                else:
                    conn.sendall(json.dumps({"status": "error", "message": "Invalid email or PIN."}).encode())

            elif action == "validate_token":
                username = request.get("username")
                token = request.get("token")

                if tokens.get(username) == token:
                    conn.sendall(json.dumps({"status": "success", "message": "Token valid."}).encode())
                else:
                    conn.sendall(json.dumps({"status": "error", "message": "Invalid token."}).encode())

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")
    finally:
        for username, connection in connected_users.items():
            if connection == conn:
                del connected_users[username]
                break
        print(f"[DISCONNECTED] {addr} disconnected.")
        conn.close()

def start_server():
    """Start the server and listen for incoming connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
