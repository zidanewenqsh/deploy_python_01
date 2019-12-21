import socket
import os
import struct
import time
img_path = r"../datas/pic/0.jpg"
f_len = os.path.getsize(img_path)
print(f_len)
bufsize=1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',12345))
# with open(img_path, 'rb') as f:
f = open(img_path, 'rb')
d = f.read(f_len)
# print(d)

datas = struct.pack(f">II{f_len}s", 0x12345678, f_len, d)
str = struct.pack("ii", 20, 400)
print(datas)
a1, a2 = struct.unpack("ii", str)
# print(a1)
# print(a2)
# print(s.recv(4))
for _ in range(3):
    # s.send(datas)
    s.send("world".encode())
    data = s.recv(bufsize)
    a = data.decode("utf-8")
    print("client:", a)
    # print(int(data))
    # continue
    # c, addr = s.accept()
    # magic = struct.unpack(f">I",c.recv(4))[0]
    # print(hex(magic))
f.close()