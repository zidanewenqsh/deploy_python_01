#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket_tcpip 模块
from socket import *
import struct
import pickle
import torch
from PIL import Image

bufer_size = 1024
back_log = 5
tcp_server = socket(AF_INET, SOCK_STREAM)  # 创建 socket_tcpip 对象
# host = gethostname()  # 获取本地主机名
# port = 12345  # 设置端口
ip_port = ("192.168.1.35", 12345)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 当两个socket的address和port相冲突，而你又想重用地址和端口
tcp_server.bind(ip_port)  # 绑定端口

tcp_server.listen(back_log)  # 等待客户端连接
while True:

    conn, addr = tcp_server.accept()  # 建立客户端连接
    print("双向链接是", conn)
    print('连接地址：', addr)
    while True:
        try:
            data1 = struct.unpack(">I", conn.recv(4))[0]
            if not data1:
                break
            print("客户端发来的信息1是：", data1)
            da_len = struct.unpack(">I", conn.recv(4))[0]
            print("客户端发来的信息2是：", da_len)


            if da_len>bufer_size:
                recv_size = 0
                recv_msg = b''
                while recv_size < da_len:
                    recv_msg += conn.recv(bufer_size)
                    recv_size = len(recv_msg)
            else:
                recv_msg = conn.recv(da_len)

            data = pickle.loads(recv_msg)
            # print(str(data))
            print("客户端发来的信息3是：",data) #接收数据
            conn.send("ok".encode())
            # d1 = struct.unpack(">I", conn.recv(4))[0]
            # print("客户端发来的信息4是：", d1)
            # d2 = struct.unpack(">I", conn.recv(4))[0]
            # print("客户端发来的信息5是：", d2)

        except Exception as e:
            print(e)
            break

    conn.close()  # 关闭连接
tcp_server.close()
