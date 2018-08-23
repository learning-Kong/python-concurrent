# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

#写一个程序，要求用户输入用户名和密码，要求密码长度不少于6个字符，且必须以字母开头，如果密码合法，则将该密码使用md5算法加密后的十六进制概要值存入名为password.txt的文件，超过三次不合法则退出程序；

import re
import hashlib
import json

def check():
    num = 0
    while num <= 2:
        user_name = input('pls input your name').strip()
        user_password = input('ple input your password').strip()
        if len(user_password) >= 6 and re.search('^([a-z]|[A-Z])',user_password):
            md5_user_pass = hashlib.md5(user_password.encode('utf-8')).hexdigest()
            user_info = {"name":user_name,"pass":md5_user_pass}
            with open('password.txt','w') as fp:
                json.dump(user_info,fp)
            break
        else:
            print("pls input again")
            num +=1
    else:
        print("you have no chance!!!")
if __name__ == "__main__":
    check()