# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

#写一个程序，使用socketserver模块，实现一个支持同时处理多个客户端请求的服务器，要求每次启动一个新线程处理客户端请求；

import socketserver
from threading import currentThread

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        flag = True
        while flag:
            try:
                data = self.request.recv(1024)
                print (currentThread().getName())
                print (data.decode('utf-8'))
                if data.decode('utf-8') == 'exit':
                    flag = False
                else:
                    self.request.send(data.upper())
            except Exception as e:
                print (e)
                flag = False


if __name__ == "__main__":
    print ('...........')
    server = socketserver.ThreadingTCPServer(('127.0.0.1',1994),Myserver)
    server.serve_forever()