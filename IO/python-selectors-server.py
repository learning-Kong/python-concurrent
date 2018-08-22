# -*- coding:utf-8 -*-
# author: "XiangLei Kong"


# https://www.cnblogs.com/yinheyi/p/8127871.html

from socket import *
import selectors

sel = selectors.DefaultSelector()       #自动选择为当前环境中最有效的Selector

def accept(server_fileobj,mask):
    conn,addr = server_fileobj.accept()
    sel.register(conn,selectors.EVENT_READ,read)    #EVENT_READ ：      表示可读的； 它的值其实是1；
                                                    #EVENT_WRITE：      表示可写的； 它的值其实是2；

def read(conn,mask):
    try:
        data = conn.recv(1024)
        if not data:
            print ('closing',conn)
            sel.unregister(conn)                #注销一个已经注册过的文件对象；
            return
        conn.send(data.upper()+b'_six_six')
    except Exception:
        print ('closing',conn)
        sel.unregister(conn)
        conn.close()


server_fileobj = socket(AF_INET,SOCK_STREAM)
server_fileobj.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server_fileobj.bind(('127.0.0.1',1995))
server_fileobj.listen(5)
server_fileobj.setblocking(False)   #设置socket的接口为非阻塞
sel.register(server_fileobj,selectors.EVENT_READ,accept)    #注册一个文件对象,相当于网select的读列表里append了一个文件句柄,server_fileobj,并且绑定了一个回调函数accept

while True:
    print("waiting......")
    events = sel.select()       #用于选择满足我们监听的event的文件对象； 本例中为 ：检测所有的fileobj，是否有完成wait data的
    for sel_obj,mask in events:
        print (sel_obj)
        print (mask)
        callback = sel_obj.data             #callback=accept
        callback(sel_obj.fileobj,mask)      #accpet(server_fileobj,1)