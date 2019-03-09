# -*- coding: utf-8 -*-
"""
Created on Mon Aug 06 16:57:40 2018

@author: Administrator
"""

__author__ = 'gao->ilvcr'


pathsource = 'C:\\Users\\Administrator\\Desktop\\source.txt'
pathresult = 'C:\\Users\\Administrator\\Desktop\\result.txt'

def countnum():
    '''
        count data number in a file
    '''
    count = 0
    with open(pathsource, 'r') as sor:
        for index, line in enumerate(sor):
            count += 1        
        #print("Count data number in a file is {}".format(count))
    
    return count


def formatdata(count):
    '''
        format data in origindata 
        rules: Data is grouped in ten groups for equalization           
    '''
    curr = 0
    divisor = 10
    with open(pathsource, 'r') as sor:
        with open(pathresult, 'w') as rel:
            
            so = sor.readlines()
            
            for curr in range(count-1):
                for i in range(divisor):
                    if curr % divisor == 0:                    
                        so[curr+i] = so[curr]
            
            for relt in so:
                rel.write(relt)
    
    
if __name__ == '__main__':
    count = countnum()
    print("Count data number in a file is {}".format(count))    
    formatdata(count)