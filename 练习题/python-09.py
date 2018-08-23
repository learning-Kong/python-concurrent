# -*- coding: utf-8 -*-
# author: "XiangLei Kong"

#写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；

from threading import Thread
import time

def func(name):
    print (name,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

if __name__ == '__main__':
    print ('主线程',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    time.sleep(10)
    for i in range(10):
        t = Thread(target=func,args=('第%s线程'% i,))
        t.start()