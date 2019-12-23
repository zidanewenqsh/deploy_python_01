import socket
import os
import struct
import time
import numpy as np
import torch
import pickle

bufer_size = 1024
img_path = r"../datas/pic/0.jpg"
a = torch.arange(100)
da = pickle.dumps(a)
da_len = len(da)
print(len(da))

f_len = os.path.getsize(img_path)
# print(f_len)
bufsize = 1024
# ip_port = ("192.168.1.35", 12345)
ip_port = ("192.168.1.15", 12345)

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(ip_port)
for i in range(5):
    print("i", i)
    datas = struct.pack(f">II{da_len}s", 0x12345678, da_len, da)
    # datas = struct.pack(f">ii{da_len}sII", 0x12345678, da_len, da, 1, 1)
    # datas = struct.pack(f">II", 0x12345678, da_len)
    tcp_client.send(datas)
    # recv1 = tcp_client.recv(bufer_size)
    # print(recv1)

tcp_client.close()
