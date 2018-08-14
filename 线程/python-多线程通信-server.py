# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

from threading import Thread
import subprocess
import socket

def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            obj = subprocess.Popen(data.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            data_out = obj.stdout.read()
            data_err = obj.stderr.read()
            if len(data_err) != 0:break
            conn.send(data_out)
        except Exception as e:
            print (e)
            break


def Server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1',1994))
    server.listen(5)

    while True:
        conn,addr = server.accept()
        t = Thread(target=talk,args=(conn,))
        t.start()

    server.close()

if __name__ == "__main__":
    Server()