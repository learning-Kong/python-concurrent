# -*- coding: utf-8 -*-
# author: "XiangLei Kong"


from greenlet import greenlet
import time

# eta
def eat(name):
    print('%s eat 1' % name)
    time.sleep(10)
    g2.switch('kong')
    print('%s eat 2' % name)
    g2.switch()

def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)

g1 = greenlet(eat)      # 创建一个greenlet对象
g2 = greenlet(play)

g1.switch('alex')   # 开关： run greenlet对象
