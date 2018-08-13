# -*- conding:utf-8 -*-
# author: "Xianglei Kong"


#（1） p.is_alive(): 查看进程是否存活
from multiprocessing import Process
import time

def task(name):
    print ("%s is running" % name)
    time.sleep(2)
    print ("%s is done" % name)

if __name__ == '__main__':
    p = Process(target=task,args=('子进程',))
    p.start()
    print (p.is_alive())
    p.join()

    print('主进程done')
    print(p.is_alive())

#(2) p.terminate() 关闭进程但不会立即关闭
from multiprocessing import Process
import time

def task(name):
    print ("%s is running" % name)
    time.sleep(2)
    print ("%s is done" % name)

if __name__ == '__main__':
    p = Process(target=task,args=('子进程',))
    p.start()
    print (p.is_alive())

    p.terminate()           #关闭进程，但不会立刻关闭
    print (p.is_alive())
    time.sleep(3)
    print (p.is_alive())
    p.join()

    print('主进程done')
    print(p.is_alive())

#（3）name='子进程1'：可以用关键参数来指定进程名，系统的系统名
from multiprocessing import Process
import time

def task (name):
    print ("%s is running" % name)
    time.sleep(2)
    print ("%s is done" % name)

if __name__ == '__main__':
    p = Process(target=task,args=("子进程",),name="111的进程")
    p.start()
    print (p.name)      #获取进程名  p.name
    p.join()
    print ('主进程done')

#（4）p.pid： 查看进程的pid
from multiprocessing import Process
import time
import os

def task(name):
    print ("%s is running" % name,os.getpid())
    time.sleep(2)
    print ("%s is done" % name)

if __name__ == "__main__":
    p = Process(target=task,args=('子进程',),name='111的进程')

    p.start()
    print (p.pid)

    print ('主进程done')