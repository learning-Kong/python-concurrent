# -*- coding: utf-8 -*-
# author; "XiangLei Kong"


#---------------------------------------------进程池-------------------------------------------------------------

# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os
# import time
#
# def task(name):
#     print ("%s is running <pid: %s>" % (name,os.getpid()))
#     time.sleep(2)
#
# if __name__ == "__main__":
#
#     pool = ProcessPoolExecutor(4)       # 进程池max_workers：4个
#     for i in range(10):             # 总共执行10次，每次4个进程的执行
#         pool.submit(task,'子线程%s' % i)           #异步提交任务
#     pool.shutdown(wait=True)            # join()方法，等待子进程执行完成，才继续执行下面
#     #pool.shutdown(wait=False)          #立即返回，执行下面的语句
#     print("master")

#--------------------------------------------线程池--------------------------------------------------------------

# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# from threading import current_thread
# import os
# import time
#
# def task():
#     print ('%s is running 《pid: %s》' % (current_thread().getName(),os.getpid()))
#     time.sleep(2)
#
# if __name__ == "__main__":
#     pool = ThreadPoolExecutor(4)
#     for i in range(10):
#         pool.submit(task)
#     pool.shutdown(wait=True)
#
#     print ("主")

#---------------------------------------------------map取代for+submit-------------------------------------
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# from threading import current_thread
# import os
# import time
#
# def task(n):
#     print ('%s is running 《pid: %s》' % (current_thread().getName(),os.getpid()))
#     time.sleep(2)
#
# if __name__ == "__main__":
#     pool = ThreadPoolExecutor(5)
#     # for i in range(10):
#     #     pool.submit(task)
#     pool.map(task,range(1,11)) # 认清局限性和妙用
#     pool.shutdown(wait=True)
#
#     print ("主")

#----------------------------------------------异步调用与回调机制---------------------------------------------

# 提交任务的两种方式
# 1、同步调用     提交完任务后，拿到结果，再执行下一行代码，导致程序是串行执行
# 2、异步调用    提交完任务后，不用等待任务执行完毕
# from concurrent.futures import ThreadPoolExecutor
# import time
# import random
#
#
# # 吃饭
# def eat(name):
#     print('%s is eat' % name)
#     time.sleep(random.randint(1,5))
#     ret = random.randint(7, 13) * '#'
#     return {'name': name, 'ret': ret}
#
#
# # 称重
# def weight(body):
#     name = body['name']
#     size = len(body['ret'])
#     print('%s 现在的体重是%s' %(name, size))
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(15)
#
#     rice1 = pool.submit(eat, 'alex').result()   #　取得结果       # 执行函数eat
#     weight(rice1)                                               # 执行函数weight
#
#     rice2 = pool.submit(eat, 'jack').result()
#     weight(rice2)
#
#     rice3 = pool.submit(eat, 'tom').result()
#     weight(rice3)
#
