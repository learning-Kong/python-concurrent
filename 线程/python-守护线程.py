# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

from threading import Thread
import time

def task(name):
    print ('%s is running' % name)
    time.sleep(2)
    print('%s is done' % name)

if __name__ == "__main__":
    t = Thread(target=task,args=('子线程1',))
    t.daemon=True
    t.start()

    print('主done')          #注意守护线程，jion，和正常start 三种线程运行的方式