# -*- coding:utf-8 -*-
# author: "XiangLei Kong"


#（1）---------------------------------------- 开进程的开销远远大于开线程------------------------------------------

# import time
# import random
# from multiprocessing import Process
# from threading import Thread
#
#
# def task(name):
#     print ("%s is running" % name)
#     time.sleep(random.randint(1,4))
#     print('%s is done' % name)
#
#
# if __name__ == "__main__":
#     p = Process(target=task,args=('子进程',))
#     p.start()       #p.start ()将开启进程的信号发给操作系统后，操作系统要申请内存空间，让好拷贝父进程地址空间到子进程，开销远大于线程
#
#     t = Thread(target=task,args=('子线程',))
#     t.start()       #t.start ()的同时就将线程开启了，然后先打印出了hello，证明线程的创建开销极小
#     print ('主done')


#（2）-------------------------------同一个进程的多个线程共享该进程的地址空间-------------------------------------

# from multiprocessing import Process
# n = 100
#
# def task():
#     global n
#     n = 0
#
# if __name__ == "__main__":
#     p = Process(target=task)        #进程之间地址空间是隔离的
#     p.start()                       #毫无疑问子进程p已经将自己的全局的n改成了0,但改的仅仅是它自己的,查看父进程的n仍然为100
#
#     print ('主进程n的值：',n)

# from threading import Thread
#
# n = 100
#
# def task():
#     global n
#     n = 0
#
# if __name__ == "__main__":
#     t = Thread(target=task)     #同一进程内开启的多个线程是共享该进程地址空间的
#     t.start()                   #执行结果如下， 查看结果为0,因为同一进程内的线程之间共享进程内的数据
#
#     print("主进程n的值: ",n)

#-------------------------------------------------（3）查看pid--------------------------------------------

#current_process().pid：也可查看线/进程的id，不能查看父id
#os.getpid()  查看进程/线程id
#os.getppid()    查看进程/线程的父id

# from multiprocessing import Process,current_process
#
# def task():
#     print ('子pid：',current_process().pid)
#
# if __name__ == "__main__":
#     p = Process(target=task)
#     p.start()       #开多个进程,每个进程都有不同的pid
#
#     print("父pid：",current_process().pid)

from threading import Thread
from multiprocessing import current_process
import os

def task():
    print ('子线程pid：',current_process().pid)
    print ("子线程pid：",os.getpid())
    print('父线程pid：',os.getppid())

if __name__ == '__main__':
    t = Thread(target=task)
    t.start()           #在主进程下开启多个线程,每个线程都跟主进程的pid一样

    print ('父进程pid：',current_process().pid)