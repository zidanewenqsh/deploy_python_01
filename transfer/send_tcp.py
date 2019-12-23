import socket
import os
import struct
import time
import numpy as np
import torch
import pickle

'''
传输文件'''

class Send_path():
    def __init__(self, ip_port, bufsize, src_path):
        self.ip_port = ip_port
        self.bufsize = bufsize
        self.src_path = src_path

    def send_path(self):
        src_path = os.path.abspath(self.src_path)
        if os.path.isfile(src_path):
            roots = os.path.dirname(self.src_path)
            file_name = os.path.basename(self.src_path)
            self.send_file(roots, file_name, src_path, self.ip_port, self.bufsize)
        elif os.path.isdir(src_path):
            for roots, dirs, files in os.walk(src_path):
                # file_path = os.path.join(roots, files)
                for file_name in files:
                    self.send_file(roots, file_name, src_path, self.ip_port, self.bufsize)
    @staticmethod
    def send_file(roots, file_name, src_path, ip_port, bufsize):
        file_path = os.path.join(roots, file_name)
        # dir_rel = '\\'.join(os.path.dirname(file_path).split('\\')[1:])
        dir_rel = os.path.dirname(file_path)[len(src_path) + 1:]  # 获取相对文件夹路径

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


if __name__ == '__main__':
    bufsize = 1024
    ip_port = ("192.168.1.15", 12355)
    # src_path = r"D:\PycharmProjects\deploy_python_01\datas"
    src_path = r"D:\PycharmProjects\deploy_python_01\transfer\strtest.py"
    s = Send_path(ip_port, bufsize, src_path)
    s.send_path()
