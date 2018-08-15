# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

# from threading import Thread
# import time
#
# def task(name):
#     print ('%s is running' % name)
#     time.sleep(2)
#     print('%s is done' % name)
#
# if __name__ == "__main__":
#     t = Thread(target=task,args=('子线程1',))
#     t.daemon=True
#     t.start()
#
#     print('主done')          #注意守护线程，jion，和正常start 三种线程运行的方式

#练习思考下述代码的执行结果有可能是哪些情况？为什么？

from threading import Thread
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
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")