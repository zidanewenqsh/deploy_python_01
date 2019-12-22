from socket import *
import struct
import os
import torch
import pickle

ip_port=('127.0.0.1',8080)
back_log=5
bufer_size = 1024

a = torch.arange(100)
da = pickle.dumps(a)
da_len = len(da)

udp_client=socket(AF_INET,SOCK_DGRAM)
for i in range(1):
    print("i", i)
    f_infosize = struct.calcsize("128sl")
    print(f_infosize)
    start = '1'.encode('utf-8')
    udp_client.sendto(start, ip_port)
    infos = struct.pack(f">II128s", 0x12345678, da_len, da)
    udp_client.sendto(infos, ip_port)

udp_client.close()


