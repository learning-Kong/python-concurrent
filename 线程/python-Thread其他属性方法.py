# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

#Thread实例对象的方法
  # isAlive(): 返回线程是否活动的。
  # getName(): 返回线程名。
  # setName(): 设置线程名。

#threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程变量。
  # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

#-------------------------------------(1)currnet.Thread.getName() 当前线程名称-------------------------------------

# from threading import Thread,current_thread
# import time
#
# def task():
#     print ('%s is running' % current_thread().getName())        # 返回当前线程名称
#     time.sleep(1)
#     print ('%s is done' % current_thread().getName())
#
# if __name__ == "__main__":
#     t = Thread(target=task)
#     t.start()
#
#     print (t.getName())  # 线程名：Thread-1
#     print ('当前线程名称',current_thread().getName())

#------------------------------------------------（2）自定义线程名称----------------------------*------------------
# from threading import Thread,current_thread
# import time
#
# def task():
#     print ("%s is running" % current_thread().getName())
#     time.sleep(1)
#     print ("%s is done" % current_thread().getName())
#
# if __name__ == '__main__':
#     t = Thread(target=task,name='子线程9999')            #自定义线程名称方法一
#     t.start()
#
#     print(t.getName())
#     current_thread().setName('父线程8888')               #自定义线程方法二
#     print ('当前线程名：',current_thread().getName())


#-------------------------------------------------（3）isAlive() / is_alive()-------------------------------
# from threading import Thread,current_thread
# import time
#
# def task():
#     print ("%s is running" % current_thread().getName())
#     time.sleep(1)
#     print ("%s is done" % current_thread().getName())
#
# if __name__ == "__main__":
#     t = Thread(target=task,name="子线程9999")
#     t.start()
#
#     print(t.is_alive())         #检测线程是否活动方法一
#     t.join()
#     print (t.isAlive())         #检测线程是否活动方法二
#     print ('当前线程名称：',current_thread().getName())

#----------------------------------------------（4）查看活动中的线程数量---------------------------------------
# from threading import Thread,current_thread,active_count
# import time
#
# def task():
#     print ("%s is running" % current_thread().getName())
#     time.sleep(1)
#     print ("%s is done" % current_thread().getName())
#
# if __name__ == '__main__':
#     t = Thread(target=task,name='子线程9998')
#     t1 = Thread(target=task, name='子线程9999')
#     t.start()
#     t1.start()
#
#     print(t.is_alive())
#     print(active_count())
#     t.join()
#     t1.join()
#     print(t.isAlive())
#     print(active_count())
#
#     print('当前线程名称',current_thread().getName())

#-------------------------------------------（5）正在运行线程list----------------------------------------------
from threading import Thread,current_thread
import threading
import time

def task():
    print('%s is running' % current_thread().getName())
    time.sleep(1)
    print('%s is done' % current_thread().getName())

if __name__ == '__main__':
    t = Thread(target=task,name='子线程9999')
    t.start()

    print(threading.enumerate())