import socket
import os
import struct
import time
import numpy as np
import torch
import pickle
'''
传输文件'''


bufer_size = 1024
file_path = r"D:\PycharmProjects\deploy_python_01\socket_tcpip\TcpclientTest_file.py"
# file_name = file_path.split('/')[-1]
file_name = os.path.basename(file_path).encode('utf-8')
print(file_name)
f_len = os.path.getsize(file_path)
print(f_len)
a = os.stat(file_path).st_size # 跟上面应该一样
print(a)

bufsize = 1024
ip_port = ("192.168.1.15", 12355)

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(ip_port)
for i in range(1):
    print("i", i)
    f_infosize = struct.calcsize("128sl")
    print(f_infosize)

    infos = struct.pack(f">II128s", 0x12345678, f_len, file_name)
    tcp_client.sendall(infos)

    with open(file_path, 'rb') as f:
        # datas = struct.pack(f">III{name_len}s{f_len}s", 0x12345678, f_len, name_len, file_name.encode("utf-8"), f.read())
        tcp_client.send(f.read())


        data1 = tcp_client.recv(bufer_size).decode('utf-8')
        print(data1)
tcp_client.close()
