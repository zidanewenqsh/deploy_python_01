#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket_tcpip 模块
import struct
bufsize= 1024
s = socket.socket()  # 创建 socket_tcpip 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind(('127.0.0.1', port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    # if not s.accept():
    #     print("no")
    #     break
    # else:
    #     print("yes")
    c, addr = s.accept()  # 建立客户端连接
    print(c)

    print('连接地址：', addr)

    # c.send('欢迎访问菜鸟教程！'.encode())
    # magic = struct.unpack(">I",c.recv(4))[0]
    # print(hex(magic))
    # print(type(magic))
    # c.send("hello".encode('utf-8'))
    # print(bytes(magic))
    # data = c.recv(bufsize)
    # data = 0

    # if data:=c.recv(bufsize):
    #     print("sever", c.recv(bufsize).decode())
    #     c.send("hello".encode())
    # else:
    #     print("None")


c.close()  # 关闭连接