# -*- coding: utf-8 -*-
"""
Created on Fri Sep 07 14:34:48 2018

@author: gao->ilvcr
"""

__author__ = 'gao->ilvcr'


pathsource = 'C:\\Users\\Administrator\\Desktop\\addoneonacolresult.txt'


def adddfonacol(begin, end):
    Jan = end - begin    
    reqlist = []
    beforeadd = 158.06
    with open(pathsource, 'w+') as sor:
        for data in range(Jan):
            beforeadd += 1.1
            reqlist.append(beforeadd)            
            
        for data in reqlist:
            print data            
            #sor.write(str(data)+'\n')
                       
if __name__ == '__main__':
    adddfonacol(4095, 5017)



