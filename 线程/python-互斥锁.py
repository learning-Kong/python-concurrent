# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

# from threading import Thread
# import threading
# import time
#
# n = 100
#
# def task():
#     global n
#     temp = n
#     time.sleep(0.01)
#     n = temp-1
#     print(n)
#
# if __name__ == "__main__":
#     t_1 = []
#     for i in range(100):
#          t = Thread(target=task)
#          t_1.append(t)
#          t.start()
#     for j in t_1:
#         j.join()
#     print ('主done',threading.enumerate())       #------------并行数据同样会失真--------------



from threading import Thread,Lock
import os,time
def work():
    global n
    lock.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    print(n)
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    n=100
    l=[]
    for i in range(100):
        p=Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n) #结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全，不加锁则结果可能为99