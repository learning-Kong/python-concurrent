# -*- coding: utf-8 -*-
# author: "XiangLei Kong"


from greenlet import greenlet

# eta
def eat(name):
    print('%s eat 1' % name)
    print('%s eat 2' % name)

def play(name):
    print('%s play 1' % name)
    print('%s play 2' % name)

g1 = greenlet(eat)      # 创建一个greenlet对象
g2 = greenlet(play)

g1.switch('alex')   # 开关： run greenlet对象
