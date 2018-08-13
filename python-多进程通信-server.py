# -*-conding:utf-8 -*-
# author: "XiangLei Kong"

import socket
from multiprocessing import Process
import subprocess

def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            print ("recv_data",data.decode('utf-8'))
            if not data:break
            obj = subprocess.Popen(data.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            data_send = obj.stdout.read()
            data_err = obj.stderr.read()
            if len(data_err) != 0:break
            conn.send(data_send)
        except Exception as e:
            print (e)

def server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',1994))
    server.listen(5)

    while True:
        conn,addr = server.accept()
        P = Process(target=talk,args=(conn,))
        P.start()
    server.close()

if __name__ == '__main__':
    server()