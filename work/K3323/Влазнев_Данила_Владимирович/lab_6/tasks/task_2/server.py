import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))
s.listen(1)

def hip(a, b):
    return float((a ** 2 + b ** 2) ** 0.5)


while True:
    client_socket, address = s.accept()
    try:
        data = client_socket.recv(1024)
        if data:
            decoded = data.decode('utf-8')
            pif_a, pif_b = map(float, decoded.split(' '))
            client_socket.send(f"{hip(pif_a, pif_b)}".encode('utf-8'))
    except KeyboardInterrupt:
        s.close()
