# -*- coding:utf-8 -*-
# author : "Xianglei Kong"

# 守护进程注意事项：
#其一：守护进程会在主进程代码执行结束后就终止

#其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children

#应用场景：如果子进程的任务在主进程任务结束后就没有存在的必要了，那么该子进程应该在开启前就被设置成守护进程。主进程代码运行结束，守护进程随即终止

from multiprocessing import Process
import time
import random

def task(name):
    print ('%s is running' % name)
    time.sleep(random.randrange(1,3))
    print ('%s is done' % name)

if __name__ == '__main__':
    p = Process(target=task,args=('Kong',))
    p.daemon=True   #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()
    print ('主')#只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了

#练习题：思考下列代码的执行结果有可能有哪些情况？为什么？
from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")