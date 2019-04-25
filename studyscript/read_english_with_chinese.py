#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: read_english_with_chinese.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 25 14:43:43 2019
# Description: 中英文电子书对照阅读,从英文电子书中读取一句(以点分割),中文读取一句(以句号分割),最后组合
#************************************************************************#


def read_english_with_chinese():
    
    with open('Englist.txt', 'r') as f:
        English = f.read()

    with open('Chinese.txt', 'r') as f:
        Chinese = f.read()


    Ens = English.split('.')
    Chs = Chinese.split(u'。')
    
    ans = ""
    index = 0
    print len(Chs), len(Ens)

    Chs.append("")
    for i in Ens:
        ans += i + '.' + Chs[index] + u'。' + '\n'
        index += 1

    print ans
    input()


