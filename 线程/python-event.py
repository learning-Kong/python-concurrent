# -*- coding: utf-8 -*-
# author: "XiangLei Kong"

# event.isSet()：返回event的状态值；
# event.wait(timeout)：堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
# event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
# event.clear()：恢复event的状态值为False。

# from threading import Thread,Event
# import time
#
# event = Event()
#
# def student (name):
#     print ('学生%s is learning' % name)
#     event.wait()            #如果一个线程等待一个已经被设置为真的Event对象,那么它将忽略这个事件, 继续执行
#     print(event.is_set())
#     print ('学生%s is sleep' % name)
#
# def teacher(name):
#     print ('%s teacher is teaching' % name)
#     time.sleep(3)
#     event.set()             #一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。
#
# if  __name__ == "__main__":
#     for i in range(1,4):
#         t = Thread(target=student,args=(i,))
#         t.start()
#
#     t = Thread(target=teacher,args=('kong',))
#     t.start()

#----------------------------------------------模拟连接数据库代码-----------------------------------------------------
# from threading import Thread,Event
# import threading
# import time,random
#
# event = Event()
# def conn_mysql():
#     count=1
#     while not event.is_set():
#         if count > 3:
#             raise TimeoutError('链接超时')
#         print ('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
#         event.wait(0.5)
#         count+=1
#     print ('<%s>链接成功' %threading.current_thread().getName())
#
# def check_mysql():
#     print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
#     time.sleep(random.randint(2,4))
#     event.set()
#
# if __name__ == "__main__":
#     conn1=Thread(target=conn_mysql)
#     conn2=Thread(target=conn_mysql)
#     check=Thread(target=check_mysql)
#
#     conn1.start()
#     conn2.start()
#     check.start()

#------------------------------------------定时器----------------------------------------------
#定时器，指定n秒后执行某操作

# from threading import Timer
#
# def hello():
#     print ("hello world")
# t = Timer(1,hello)
# t.start()

#--------------------------------------------模拟验证码-------------------------------------
from threading import Timer
import random

class Code():
    def __init__(self):
        self.make_cache()
        print (1)

    def make_cache(self,interval=5):
        self.cahce = self.make_code()
        print (self.cahce)
        self.t = Timer(interval,self.make_cache)        #循环镶嵌调动
        self.t.start()
    def make_code(self,n=4):
        ret = ''
        for i in range(n):
            s1 = str(random.randint(0,9))
            s2 = chr(random.randint(65,90))
            ret += random.choice([s1,s2])
        return ret

    def check(self):
        while True:
            code = input('输入验证码>>>: ').strip()
            if code.upper() == self.cahce:
                print('输入成功')
                self.t.cancel()
                break

obj = Code()
obj.check()