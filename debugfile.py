#!/usr/bin/python
# -*- coding=utf-8 -*-
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @FileName: debugfile.py
# @IncludeProject: myscript
# @IDEName: PyCharm
# @Version: None
# @Author: gao->ilvcr
# @Mail: liyaoliu@foxmail.com @@ ilvcr@outlook.com
# @CreatedTime: 07/17/2019 @ 21:33
# @Description: 
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import random
import string

p = "".join([random.choice(string.ascii_letters) for i in range(5)])
q = "".join([random.choice(string.ascii_letters + string.hexdigits) for i in range(6)])
print(p)
print(q)
# p,q就是初始化的用户和密码,p是用户名,q是密码，可以打印，可以不打印

# flag，count是计数器
flag = 0
count = 0
while True:

    username = input("输入你的名字")
    if username == p:
        while True:
            passwd = input("输入你的密码")
            if passwd == q:
                print("成功进入")
                break
            else:
                flag += 1
            if flag == 3:
                break
    else:
        count += 1
    if count == 3:
        break
#    break   这个break是为了控制用户输入正确密码还让用户输入不
