# -*- conding:utf-8 -*-
# author: "Xianglei Kong"

from multiprocessing import Process,Queue
import time,random,os

def producer(name,q):
    for i in range(10):
        time.sleep(0.5)
        print('生产者%s生产了 包子[%s]' % (name, i))
        q.put('包子[%s]' % i)

def producer2(name,q):
    for i in range(10):
        time.sleep(0.5)
        print('生产者%s生产了 面条[%s]' % (name, i))
        q.put('面条[%s]' % i)

def consumer(name,q):
    while True:
        ret = q.get()
        if ret is None:break
        print('消费者%s吃了 %s' % (name, ret))

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer,args=('ales',q))
    p2 = Process(target=producer2, args=('lin', q))
    p3 = Process(target=producer, args=('kong', q))

    c1 = Process(target=consumer, args=('jack',q))
    c2 = Process(target=consumer, args=('jack2', q))

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    p1.join()           #等待生产者函数进程执行完成
    p2.join()           #等待生产者函数进程执行完成
    p3.join()           #等待生产者函数进程执行完成

    q.put(None)         #queue放入None，#两个消费者，放入两个None即可
    q.put(None)         #queue放入None

from multiprocessing import JoinableQueue,Process
import time

def producer(name,q):
    for i in range(10):
        print('生产者%s生产了 包子[%s]' % (name, i))
        q.put('包子[%s]' % i)
    q.join()


def consumer(name,q):
    while True:
        ret = q.get()
        print ("消费者%s吃了 %s" %(name,ret))
        q.task_done()   # 发送信号给q.join()，说明已经从队列中取走一个数据并处理完毕了

# 开启进程函数
if __name__ == '__main__':
    q = JoinableQueue()

    # 生产者
    p1 = Process(target=producer,args=('kong1',q))
    p2 = Process(target=producer, args=('kong2', q))
    p3 = Process(target=producer, args=('kong3', q))

    # 消费者们
    c1 = Process(target=consumer,args=('luo1',q))
    c2 = Process(target=consumer,args=('luo2',q))

    c1.daemon =True
    c2.daemon=True

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()