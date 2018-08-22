# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

from socket import *
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',1995))

while True:
    msg=input('>>: ')
    if not msg:continue
    c.send(msg.encode('utf-8'))
    data=c.recv(1024)
    print(data.decode('utf-8'))