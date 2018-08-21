# -*- coding:utf-8 -*-
# author "XiangLei Kong"

#用法
# g1=gevent.spawn(func,1,,2,3,x=4,y=5)创建一个协程对象g1，spawn括号内第一个参数是函数名，如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的
#
# g2=gevent.spawn(func2)
#
# g1.join() #等待g1结束
#
# g2.join() #等待g2结束
#
# #或者上述两步合作一步：gevent.joinall([g1,g2])
#
# g1.value#拿到func1的返回值

# import gevent
# import time
# def eat(name):
#     print('%s eat 1' % name)
#     gevent.sleep(0.5)
#     # time.sleep(2)           #gevent 不能直接识别除gevent.sleep()之外的柱阻塞，虚打补丁
#     print('%s eat 2' % name)
#
# def play(name):
#     print('%s play 1' % name)
#     gevent.sleep(2)
#     # time.sleep(2)           #gevent 不能直接识别除gevent.sleep()之外的柱阻塞，虚打补丁
#     print('%s play 2' % name)
#
# g1 = gevent.spawn(eat,'luo')
# g2 = gevent.spawn(play,'kong')
#
# gevent.joinall([g1,g2])

#---------------------------------------------gevent补丁--------------------------------------------------
# 上例gevent.sleep(2)模拟的是gevent可以识别的io阻塞,
#
# 而time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了
#
# from gevent import monkey;monkey.patch_all()必须放到被打补丁者的前面，如time，socket模块之前
#
# 或者我们干脆记忆成：要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头

from gevent import monkey;monkey.patch_all()
import gevent
import time


def eat(name):
    print('%s eat 1' % name)
    time.sleep(2)
    print('%s eat 2' % name)

def play(name):
    print('%s play 1' % name)
    time.sleep(2)
    print('%s play 2' % name)

g1 = gevent.spawn(eat,'luo')
g2 = gevent.spawn(play,'kong')

gevent.joinall([g1,g2])
