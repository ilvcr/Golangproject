# -*- coding: utf-8 -*-
"""
Created on Mon Aug 06 16:32:12 2018

@author: Administrator
"""

__author__ = 'gao->ilvcr'


pathsource = 'C:\\Users\\Administrator\\Desktop\\source.txt'

def countnum():
    '''
        count data number in a file
    '''
    count = 0
    with open(pathsource, 'r') as sor:
        for index, line in enumerate(sor):
            count += 1        
        print("Count data number in a file is {}".format(count))
             

if __name__ == '__main__':
    countnum()
    
    