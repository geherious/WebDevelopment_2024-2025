import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
nums = f"{a} {b}"

s.send(nums.encode('utf-8'))

msg = s.recv(1024)
umsg = msg.decode('utf-8')
print(umsg)
s.close()
