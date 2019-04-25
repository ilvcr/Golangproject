#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: file_rename.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Mon Apr 23 14:13:34 2018
# Description: 文件批量重命名
#************************************************************************#

import os

def file_rename():
    file_path = raw_input("请输入文件路径: ")
    f = os.listdir(file_path)
    n = 0
    for i in f:
        i = f[n]
        old_name = path + i
        new_name = path + i[:6] + '9' + str(n+1) + i[6:-5] + '.xlsx'
        os.rename(old_name, new_name)
        print old_name, '==========>', new_name
        n += 1

if __name__ '__main__':
    file_path

