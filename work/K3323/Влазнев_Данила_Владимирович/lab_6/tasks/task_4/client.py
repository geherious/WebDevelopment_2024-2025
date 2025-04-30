import socket
import threading


def receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("Ошибка")
            client_socket.close()
            break


def start():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    receive_thread = threading.Thread(target=receive, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'q':
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()


start()