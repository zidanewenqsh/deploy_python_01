from socket import *
import os
import struct
import pickle

save_dir = r"..\saves"
ip_port=('127.0.0.1',8080)
back_log=5
bufer_size=1024

udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)
while True:
    # while True:
    try:
        _, addr = udp_server.recvfrom(1)# 接收一个'1'，记录地址
        data1 = struct.unpack(f">I", udp_server.recvfrom(4)[0])[0]

        # if not data1:
        #     break
        print("客户端发来的信息1是：", data1)

        da_len = struct.unpack(f">I", udp_server.recvfrom(4)[0])[0]
        print("客户端发来的信息2是：", da_len)

        if da_len > bufer_size:
            recv_size = 0
            recv_msg = b''
            while recv_size < da_len:
                recv_msg += udp_server.recvfrom(bufer_size)[0]
                recv_size = len(recv_msg)
        else:
            recv_msg = udp_server.recvfrom(da_len)[0]

        data = pickle.loads(recv_msg)
        # print(str(data))
        print("客户端发来的信息3是：", data)  # 接收数据
        udp_server.send("ok".encode(),addr)

    except BaseException as e:
        print(e)
        break

udp_server.close()


