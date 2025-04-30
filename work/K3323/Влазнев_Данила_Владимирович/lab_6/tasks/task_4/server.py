import socket
import threading

users = {}

def broadcast(message, socket_from=None):
    for user, client_socket in users.items():
        if client_socket != socket_from:
            try:
                client_socket.send(message)
            except:
                client_socket.close()
                del users[user]

def try_add_user(client_socket, client_address):
    print(f"Новое подключение {client_address}")

    client_socket.send("Введите свое имя: ".encode('utf-8'))
    user_name = client_socket.recv(1024).decode('utf-8')

    if user_name in users:
        client_socket.send("Имя уже занято, подключение прервано.\n".encode('utf-8'))
        client_socket.close()
        return
    users[user_name] = client_socket

    broadcast(f"{user_name} присоединился к чату".encode('utf-8'), client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')

            if not message:
                continue

            broadcast(f"{user_name}: {message}".encode('utf-8'), client_socket)
        except:
            client_socket.close()
            del users[user_name]
            broadcast(f"{user_name} покинул чат".encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()

        client_thread = threading.Thread(target=try_add_user, args=(client_socket, client_address))
        client_thread.start()


start_server()