# -*- coding:utf-8 -*-
# author; "XiangLei Kong"

#写一个程序，包含十个线程，同时只能有五个子线程并行执行；
from threading import Thread
from threading import currentThread
from concurrent.futures import ThreadPoolExecutor
import random,time

def func(n):
    print (currentThread().getName())
    time.sleep(random.randint(2,5))

if __name__ == "__main__":
    execuotr = ThreadPoolExecutor(5)
    for i in range(10):
        execuotr.submit(func)