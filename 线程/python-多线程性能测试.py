# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

# from multiprocessing import Process
# from threading import Thread
#
# import os,time
#
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
# if __name__ == "__main__":
#     l=[]
#     print(os.cpu_count())
#     start = time.time()
#     for i in range(4):
#         p = Process(target=work)
#         #p = Thread(target=work)
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#
#     stop = time.time()
#
#     print ('run time is %s' % (stop-start))     #结论：如果并发的多个任务是计算密集型：多进程效率高

from multiprocessing import Process
from threading import Thread

import os, time


def work():
    time.sleep(2)
    print('===>')


if __name__ == "__main__":
    l = []
    print(os.cpu_count())
    start = time.time()
    for i in range(400):
        #p = Process(target=work)       #耗时9s多,大部分时间耗费在创建进程上
        p = Thread(target=work)         #耗时2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()

    stop = time.time()

    print('run time is %s' % (stop - start))            #结论：如果并发的多个任务是I/O密集型：多线程效率高

# 应用：
#
# 多线程用于IO密集型，如socket，爬虫，web
# 多进程用于计算密集型，如金融分析