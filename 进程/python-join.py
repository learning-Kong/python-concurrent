# -*- conding:utf-8 -*-
# author: "XiangLei Kong"

from multiprocessing import Process
import time
import os

def func(name):
    print ("%s is running %s" %(name,os.getpid()))
    print ("父进程ID： " ,os.getppid())
    print ("%s is done" % name)
if __name__ == '__main__':
    p = Process(target=func,args=('子进程1',))
    p.start()
    p.join()            #p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间。

    print ("父进程done:" ,os.getpid())

#-------------------------------------------进程并行测试,加强对子进程和父进程join的理解----------------------------------------
from multiprocessing import Process
import time


# 子进程函数
def task(name):
    print('%s is running' % name)
    time.sleep(2)

# 父进程代码
if __name__ == '__main__':
    start_time = time.time()
    p1 = Process(target=task, args=('子进程1',))
    p2 = Process(target=task, args=('子进程2',))
    p3 = Process(target=task, args=('子进程3',))

    p1.start()
    p2.start()
    p3.start()
    # 有的同学会有疑问: 既然join是等待进程结束, 那么我像下面这样写, 进程不就又变成串行的了吗?
    # 当然不是了, 必须明确：p.join()是让谁等？
    # 很明显p.join()是让主线程等待p的结束，卡住的是主进程而绝非子进程p，
    p1.join()
    p2.join()
    p3.join()
    print('父进程done,花费时间：',time.time()-start_time)

#---------------------------------------------进程串行测试,加强对子进程和父进程join的理解------------------------------
from multiprocessing import Process
import time


# 子进程函数
def task(name):
    print('%s is running' % name)
    time.sleep(2)

# 父进程代码
if __name__ == '__main__':
    start_time = time.time()
    p1 = Process(target=task, args=('子进程1',))
    p2 = Process(target=task, args=('子进程2',))
    p3 = Process(target=task, args=('子进程3',))

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    print('父进程done,花费时间：',time.time()-start_time)