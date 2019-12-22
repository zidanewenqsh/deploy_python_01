import socket
import os
import struct
import time
import numpy as np
import torch
import pickle

'''
传输文件'''

# file_path = r"D:\PycharmProjects\deploy_python_01\socket_tcpip\TcpclientTest_file.py"
src_dir = r"D:\PycharmProjects\deploy_python_01\datas"

bufsize = 1024
ip_port = ("192.168.1.15", 12355)

src_dir = os.path.abspath(src_dir)
for roots, dirs, files in os.walk(src_dir):
    # file_path = os.path.join(roots, files)
    for file_name in files:
        file_path = os.path.join(roots, file_name)
        # dir_rel = '\\'.join(os.path.dirname(file_path).split('\\')[1:])
        dir_rel = os.path.dirname(file_path)[len(src_dir)+1:] # 获取相对文件夹路径

        file_name_ = file_name.encode('utf-8')
        dir_rel_ = dir_rel.encode("utf-8")
        f_len = os.path.getsize(file_path)

        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client.connect(ip_port)
        for i in range(1):
            print("i", i)
            # f_infosize = struct.calcsize("128sl")
            # print(f_infosize)

            infos = struct.pack(f">II128s128s", 0x12345678, f_len, file_name_, dir_rel_)
            tcp_client.sendall(infos)

            with open(file_path, 'rb') as f:
                # datas = struct.pack(f">III{name_len}s{f_len}s", 0x12345678, f_len, name_len, file_name.encode("utf-8"), f.read())
                tcp_client.send(f.read())

            data1 = tcp_client.recv(bufsize).decode('utf-8')
            print(data1)
        tcp_client.close()
