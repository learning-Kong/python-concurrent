# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

#------------------------------------------------------死锁----------------------------------------------------------
# from threading import Thread,Lock
# import time
#
# lockA = Lock()
# lockB = Lock()
#
# class MyThread(Thread):
#
#     # def __init__(self):
#     #     super().__init__()
#     def run(self):
#         self.task_a()
#         self.task_b()
#
#     def task_a(self):
#         lockA.acquire()
#         print('\033[31m%s 拿到A锁1\033[0m'% self.name)
#
#         lockB.acquire()
#         print ('\033[32m%s 拿到B锁1\033[0m' % self.name)
#         lockB.release()
#         print ('\033[32m%s release B锁1\033[0m' % self.name)
#
#         lockA.release()
#         print('\033[31m%s release A锁1\033[0m' % self.name)
#
#     def task_b(self):
#         lockB.acquire()
#         print ('\033[33m%s 拿到B锁2\033[0m' % self.name)
#
#         lockA.acquire()
#         print ('\033[34m%s 拿到A锁2\033[0m' % self.name)
#         lockA.release()
#         print('\033[34m%s relases A锁2\033[0m' % self.name)
#
#         lockB.release()
#         print('\033[33m%s relases B锁2\033[0m' % self.name)              #多理解多线程原理，有助于理解死锁过程
#
# if __name__ == "__main__":
#     for i in range(10):
#         t = MyThread()
#         t.start()

#----------------------------------------------------递归锁-----------------------------------------------------------
# from threading import Thread,RLock
#
# lockA = lockB = RLock()         # 递归锁
# # 递归锁可以连续acquire多次，每acquire一次计数器+1，只有计数器为0时，才能被抢到
# class MyThread(Thread):
#
#     # def __init__(self):
#     #     super().__init__()
#     def run(self):
#         self.task_a()
#         self.task_b()
#
#     def task_a(self):
#         lockA.acquire()
#         print('\033[31m%s 拿到A锁1\033[0m'% self.name)
#
#         lockB.acquire()
#         print ('\033[32m%s 拿到B锁1\033[0m' % self.name)
#         lockB.release()
#         print ('\033[32m%s release B锁1\033[0m' % self.name)
#
#         lockA.release()
#         print('\033[31m%s release A锁1\033[0m' % self.name)
#
#     def task_b(self):
#         lockB.acquire()
#         print ('\033[33m%s 拿到B锁2\033[0m' % self.name)
#
#         lockA.acquire()
#         print ('\033[34m%s 拿到A锁2\033[0m' % self.name)
#         lockA.release()
#         print('\033[34m%s relases A锁2\033[0m' % self.name)
#
#         lockB.release()
#         print('\033[33m%s relases B锁2\033[0m' % self.name)
#
# if __name__ == "__main__":
#     for i in range(10):
#         t = MyThread()
#         t.start()
#-------------------------------------------------------信号量------------------------------------------------------
#信号量也是一把锁，可以指定信号量为5，对比互斥锁同一时间只能有一个任务抢到锁去执行，信号量同一时间可以有5个任务拿到锁去执行，如果说互斥锁是合租房屋的人去抢一个厕所，那么信号量就相当于一群路人争抢公共厕所，公共厕所有多个坑位，这意味着同一时间可以有多个人上公共厕所，但公共厕所容纳的人数是一定的，这便是信号量的大小

from threading import Thread,Semaphore,current_thread
import time
import random

sm = Semaphore(3)   #信号量也是一把锁，可以指定信号量 本次为3
                    #互斥锁同一时间内只能有一个任务去抢到锁去执行，信号量同一时间可以有3个任务拿到锁去执行
def task():
    sm.acquire()
    print ('%s in ' %current_thread().getName())
    # time.sleep(random.randint(1,4))
    time.sleep(1)
    sm.release()

if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()
# 解析
# Semaphore管理一个内置的计数器，
# 每当调用acquire()时内置计数器-1；
# 调用release() 时内置计数器+1；
# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
