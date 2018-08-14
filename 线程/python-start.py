# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

#-----------------------------------------------函数方式----------------------------------------------------------
from threading import Thread
import time
import random

def task(name):
    print ('%s is running' % name)
    time.sleep(random.randint(1,4))
    print ('%s is done' % name)

if __name__ == '__main__':
    t = Thread(target=task,args=('子线程',))
    t.start()

    print('主done')

#-----------------------------------------------类的继承方式----------------------------------------------------------
from threading import Thread
import time
import random

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print ('%s is running' % self.name)
        time.sleep(random.randint(1,4))
        print ('%s is done' % self.name)

if __name__ == '__main__':
    t = MyThread('子线程1')
    t.start()
    print ('主done')