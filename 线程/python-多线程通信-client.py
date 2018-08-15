# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',1994))

while True:
    data = input('>>>: ').strip()
    if len(data) == 0:continue
    client.send(data.encode('utf-8'))
    data_recv = client.recv(1024)
    if not data:break
    print(data_recv.decode('gbk'))