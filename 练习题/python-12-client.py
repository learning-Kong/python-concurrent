# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",1994))

while True:
    msg = input('pls input massage').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
