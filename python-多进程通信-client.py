# -*- conding:utf-8 -*-
# author: "XiangLei Kong"

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",1994))

while True:
    data = input(">>>: ").strip()
    if not data:continue
    client.send(data.encode('utf-8'))
    data = client.recv(1024).decode("gbk")
    if not data:break
    print(data)