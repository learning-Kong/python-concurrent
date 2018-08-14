# -*-coding:utf-8 -*-
# author:"Xianglei Kong"

#------------------------------函数方式---------------------------------------
import time
import random
from multiprocessing import Process

def piao(name):
    print('%s is running' % name)
    time.sleep(random.randrange(1,5))
    print ('%s is end' % name)

if __name__ == '__main__':
    p1 = Process(target=piao, args=('egon',))
    p2 = Process(target=piao, args=('alex',))
    p3 = Process(target=piao, args=('wupeqi',))
    p4 = Process(target=piao, args=('yuanhao',))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主进程执行结束..') #####思考为什么先打印    主进程执行结束..


#-------------------------------类方式---------------------------------------
import time
import random
from multiprocessing import Process

class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('%s is running' % self.name)
        time.sleep(random.randrange(1, 5))
        print('%s is end' % self.name)

if __name__ == '__main__':
    #实例化得到四个对象
    p1=Piao('egon')
    p2=Piao('alex')
    p3=Piao('wupeiqi')
    p4=Piao('yuanhao')

    #调用对象下的方法，开启四个进程
    p1.start() #start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主进程执行结束..')

#-----------------------------------------查看父子进程ID---------------------------------------
from multiprocessing import Process
import time
import os

# 定义子进程的函数
def talk(name):
    print('%s is running' % name, os.getpid())  # 取出子进程的id
    print('父进程id：', os.getppid())       # 取出父进程的id
    time.sleep(2)
    print('%s is done' % name)

# 执行父进程，开启子进程
if __name__ == "__main__":
    p = Process(target=talk,args=('子进程1',))
    p.start()

    print ("父进程done",os.getpid())# 该进程的id