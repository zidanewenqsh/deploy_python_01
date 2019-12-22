from socket import *
import struct
import os


ip_port=('127.0.0.1',8080)
back_log=5
bufer_size = 1024
f_path = r"../datas/pic/1.jpg"
# file_name = file_path.split('/')[-1]
f_name = os.path.basename(f_path).encode('utf-8')
print(f_name)
f_len = os.path.getsize(f_path)
print(f_len)

udp_client=socket(AF_INET,SOCK_DGRAM)
for i in range(1):
    print("i", i)
    f_infosize = struct.calcsize("128sl")
    print(f_infosize)

    infos = struct.pack(f">II128s", 0x12345678, f_len, f_name)
    udp_client.sendto(infos, ip_port)

    with open(f_path, 'rb') as f:
        # datas = struct.pack(f">III{name_len}s{f_len}s", 0x12345678, f_len, name_len, file_name.encode("utf-8"), f.read())
        udp_client.sendto(f.read(),ip_port)
        recv1, addr = udp_client.recvfrom(bufer_size)
        print(recv1.decode('gbk'))
udp_client.close()


