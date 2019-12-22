#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

# import socket_tcpip  # 导入 socket_tcpip 模块
from socket import *

buffer_size = 1024
tcp_client = socket(AF_INET, SOCK_STREAM)  # 创建 socket_tcpip 对象
# host = gethostname()  # 获取本地主机名
# port = 12345  # 设置端口
ip_port = ("127.0.0.1", 8080)

tcp_client.connect(ip_port)

while True:
    # msg = input(">>").strip()
    msg = "hello"
    # msg = "hello".strip()
    if not msg:continue
    tcp_client.send(msg.encode('utf-8'))

    print("客户端已经发送信息", msg)
    data = tcp_client.recv(buffer_size).decode('utf-8')
    # tcp_client.send(msg.encode('utf-8'))
    print("客户端接收到的信息是",data)

