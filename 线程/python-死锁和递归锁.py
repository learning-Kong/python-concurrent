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
from threading import Thread,RLock

lockA = lockB = RLock()         # 递归锁
# 递归锁可以连续acquire多次，每acquire一次计数器+1，只有计数器为0时，才能被抢到
class MyThread(Thread):

    # def __init__(self):
    #     super().__init__()
    def run(self):
        self.task_a()
        self.task_b()

    def task_a(self):
        lockA.acquire()
        print('\033[31m%s 拿到A锁1\033[0m'% self.name)

        lockB.acquire()
        print ('\033[32m%s 拿到B锁1\033[0m' % self.name)
        lockB.release()
        print ('\033[32m%s release B锁1\033[0m' % self.name)

        lockA.release()
        print('\033[31m%s release A锁1\033[0m' % self.name)

    def task_b(self):
        lockB.acquire()
        print ('\033[33m%s 拿到B锁2\033[0m' % self.name)

        lockA.acquire()
        print ('\033[34m%s 拿到A锁2\033[0m' % self.name)
        lockA.release()
        print('\033[34m%s relases A锁2\033[0m' % self.name)

        lockB.release()
        print('\033[33m%s relases B锁2\033[0m' % self.name)              #多理解多线程原理，有助于理解死锁过程

if __name__ == "__main__":
    for i in range(10):
        t = MyThread()
        t.start()

