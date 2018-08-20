# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

#-----------------------------------先进先出为队列------------------------------------
import queue

q = queue.Queue(3)
q.put('123')
q.put('ab')
q.put('dd')

print(q.get())
print(q.get())
print(q.get())

#-----------------------------------先进后出为堆栈------------------------------------

import queue

q = queue.LifoQueue(3)
q.put('123')
q.put('ab')
q.put('dd')

print(q.get())
print(q.get())
print(q.get())

#-----------------------------------优先级队列------------------------------------
import queue

q = queue.PriorityQueue(3)
q.put((20,'12'))
q.put((10,'1'))
q.put((30,'123'))

print(q.get())
print(q.get())
print(q.get())