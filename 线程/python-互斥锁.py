from threading import Thread
import threading
import time

n = 100

def task():
    global n
    temp = n
    time.sleep(0.01)
    n = temp-1
    print(n)

if __name__ == "__main__":
    t_1 = []
    for i in range(100):
         t = Thread(target=task)
         t_1.append(t)
         t.start()
    for j in t_1:
        j.join()
    print ('主done',threading.enumerate())