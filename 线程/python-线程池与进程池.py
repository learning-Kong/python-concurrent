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

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import current_thread
import os
import time

def task():
    print ('%s is running 《pid: %s》' % (current_thread().getName(),os.getpid()))
    time.sleep(2)

if __name__ == "__main__":
    pool = ThreadPoolExecutor(4)
    for i in range(10):
        pool.submit(task)
    pool.shutdown(wait=True)

    print ("主")

