import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))

s.send('GET / HTTP/1.0\r\n\r\n'.encode('utf-8'))

msg = s.recv(1024)
umsg = msg.decode('utf-8')
print(umsg)
s.close()

