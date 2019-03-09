# -*- coding: utf-8 -*-
"""
Created on Mon Aug 06 09:39:48 2018

@author: gao->ilvcr
"""

__author__ = 'gao->ilvcr'


pathsource = 'C:\\Users\\Administrator\\Desktop\\source.txt'
pathresult = 'C:\\Users\\Administrator\\Desktop\\result.txt'

def reverse():
    '''
        reverse data in study
    '''
    with open(pathsource, 'r') as sor:
        with open(pathresult, 'w') as rel:
            so = sor.readlines()
            #print(so)
            re = so[::-1]
            #print(re)
            
            for relt in re:
                rel.write(relt)

    
if __name__ == '__main__':
    reverse()
    
