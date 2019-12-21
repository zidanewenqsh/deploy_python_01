#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket_tcpip 模块
from socket import *
buffer_size = 1024
back_log = 5
tcp_server = socket(AF_INET, SOCK_STREAM)  # 创建 socket_tcpip 对象
# host = gethostname()  # 获取本地主机名
# port = 12345  # 设置端口
ip_port = ("127.0.0.1", 12300)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
tcp_server.bind(ip_port)  # 绑定端口

tcp_server.listen(back_log)  # 等待客户端连接
while True:

    conn, addr = tcp_server.accept()  # 建立客户端连接
    print("双向链接是", conn)
    print('连接地址：', addr)
    while True:
        try:
            data = conn. recv(buffer_size)
            print("客户端发来的信息是：",data)
            conn.send(data.upper().strip())
        except:
            break

    conn.close()  # 关闭连接
tcp_server.close()
