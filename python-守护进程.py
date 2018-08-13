# -*- conding:utf-8 -*-
# author : "Xianglei Kong"

# 守护进程注意事项：
#其一：守护进程会在主进程代码执行结束后就终止

#其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children

