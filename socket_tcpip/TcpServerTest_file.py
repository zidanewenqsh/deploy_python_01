#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket_tcpip 模块
from socket import *
import struct
import pickle
import torch
from PIL import Image
import os

bufer_size = 1024
back_log = 5
save_dir = r"..\saves"
tcp_server = socket(AF_INET, SOCK_STREAM)  # 创建 socket_tcpip 对象
# host = gethostname()  # 获取本地主机名
# port = 12345  # 设置端口
ip_port = ("192.168.1.35", 12355)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 当两个socket的address和port相冲突，而你又想重用地址和端口
tcp_server.bind(ip_port)  # 绑定端口

tcp_server.listen(back_log)  # 等待客户端连接
while True:

    conn, addr = tcp_server.accept()  # 建立客户端连接
    print("双向链接是", conn)
    print('连接地址：', addr)
    while True:
        try:
            data1 = struct.unpack(f">I", conn.recv(4))[0]
            # if not data1:
            #     break
            print("客户端发来的信息1是：", data1)

            f_len = struct.unpack(f">I", conn.recv(4))[0]
            print("客户端发来的信息2是：", f_len)
            # f_name = struct.unpack(f"128s", conn.recv(128))[0]
            f_name = conn.recv(128).strip(b'\00').decode("utf-8")
            print("客户端发来的信息3是：", f_name)

            if f_len>bufer_size:
                recv_size = 0
                recv_msg = b''
                while recv_size < f_len:
                    recv_msg += conn.recv(bufer_size)
                    recv_size = len(recv_msg)
            else:
                recv_msg = conn.recv(f_len)

            if recv_msg:

                conn.send("ok".encode('utf-8'))
                # 接收文件
                f_path = os.path.join(save_dir, f_name.strip())
                with open(f_path, 'wb') as f:
                    f.write(recv_msg)
                    print("write successfully")
        except Exception as e:
            print(e)
            break

    conn.close()  # 关闭连接
tcp_server.close()
