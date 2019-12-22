import socket
import os
import struct
import time
import numpy as np
import torch
import pickle

img_path = r"../datas/pic/0.jpg"
a = torch.arange(10)
da = pickle.dumps(a)
da_len = len(da)
print(len(da))

f_len = os.path.getsize(img_path)
print(f_len)
bufsize=1024
ip_port = ("127.0.0.1", 12345)

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(ip_port)
datas = struct.pack(f">II{da_len}s", 0x12345678, da_len, da)
tcp_client.send(datas)
# with open(img_path,'rb') as f:
#     datas = struct.pack(f">II{f_len}s", 0x12345678, f_len, f.read())
#     tcp_client.sendall(datas)
tcp_client.close()

