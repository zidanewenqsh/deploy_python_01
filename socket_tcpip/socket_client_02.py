import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081)) #拨通电话
while True:
    phone.send('hello'.encode('utf-8')) #发消息

    back_msg=phone.recv(1024)
    print(back_msg)

phone.close()