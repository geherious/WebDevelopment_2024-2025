import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()

data = conn.recv(1024)
print(f'Сообщение от клиента: {data.decode()}')

conn.sendall(b'Hello, client')

conn.close()
server_socket.close()
