from socket import *
import os
import struct


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

        f_len = struct.unpack(f">I", udp_server.recvfrom(4)[0])[0]
        print("客户端发来的信息2是：", f_len)
        # f_name = struct.unpack(f"128s", conn.recv(128))[0]
        f_name = udp_server.recvfrom(128)[0].strip(b'\00').decode("utf-8")
        print("客户端发来的信息3是：", f_name)

        if f_len>bufer_size:
            recv_size = 0
            recv_msg = b''
            while recv_size < f_len:
                recv_msg += udp_server.recvfrom(bufer_size)[0]
                recv_size = len(recv_msg)
        else:
            recv_msg = udp_server.recvfrom(f_len)[0]

        if recv_msg:

            udp_server.sendto("ok".encode('utf-8'), addr)
            # 接收文件
            f_path = os.path.join(save_dir, f_name.strip())
            with open(f_path, 'wb') as f:
                f.write(recv_msg)
                print("write successfully")
    except BaseException as e:
        print(e)
        break

udp_server.close()


