# -*- conding:utf-8 -*-
# author: "Xianglei Kong"

from multiprocessing import Process,Queue
import time,random,os

def producer(name,q):
    for i in range(10):
        print('生产者%s生产了 包子[%s]' % (name, i))
        q.put('包子[%s]' % i)


def consumer(name,q):
    while True:
        ret = q.get()
        if ret is None:break
        print('消费者%s吃了 %s' % (name, ret))
        # if q.empty():break

if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer,args=('ales',q))

    c = Process(target=consumer, args=('jack',q))

    p.start()
    c.start()
    p.join()
    q.put(None)
