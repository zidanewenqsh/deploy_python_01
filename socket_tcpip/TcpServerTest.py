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
ip_port = ("127.0.0.1", 12345)
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
            print("客户端发来的信息是：", data1)
            da_len = struct.unpack(">I", conn.recv(4))[0]
            print("客户端发来的信息是：", da_len)
            # data3 = struct.unpack(">I", conn.recv(bufer_size))[0]
            # data3 = conn.recv(da_len)
            # data3 = pickle.loads(data3)
            recv_size = 0
            recv_msg = b''
            print(recv_size, da_len)
            while recv_size < da_len:
                recv_msg += conn.recv(bufer_size)
                recv_size = len(recv_msg)

            if recv_msg:
                print(recv_msg)
                print("客户端发来的信息是：", pickle.loads(recv_msg)) #接收数据
                # print(pickle.loads(recv_msg))
                # 接收文件
                # with open("abc.jpg", 'wb') as f:
                #     f.write(recv_msg)
        except:
            break

    conn.close()  # 关闭连接
tcp_server.close()
