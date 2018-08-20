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

#put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((20,'12'))
q.put((10,'1'))
q.put((30,'123'))

#结果(数字越小优先级越高,优先级高的优先出队)
print(q.get())
print(q.get())
print(q.get())