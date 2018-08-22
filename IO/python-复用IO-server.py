# -*- coding: utf-8 -*-
# author: "XiangLei Kong"


# 格式：rList,wList,eList = select.select(argv1,argv2,argv3,timeout)
#
# 参数：
#
# 　　argv1：监听序列中的句柄发生变化时，则获取发生变化的句柄添加到rList序列中
#
# 　　argv2：监听序列中含有句柄时，则将该序列中所有的句柄添加到wList序列中
#
# 　　argv3：监听序列中的句柄发生错误时，则将该发生错误的句柄添加到eList序列中
#
# 　　timeout：设置阻塞时间，如果不设置则默认一直阻塞


#http://www.cnblogs.com/wupeiqi/articles/5040823.html

from socket import *
import select

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',1994))
server.listen(5)
server.setblocking(False)        #设置socket的接口为非阻塞
print ('starting...')

print (server)
inputs = [server,]
outputs = []
wdata = {}

while True:
    rlist,wlist,elist = select.select(inputs,outputs,[],0.5)
    print (wlist)
    for sock in rlist:
        if sock == server:
            conn,addr = sock.accept()
            inputs.append(conn)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    inputs.remove(sock)
                    continue
                outputs.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                inputs.remove(sock)
    for sock in wlist:
        sock.send(wdata[sock])
        outputs.remove(sock)
        wdata.pop(sock)

