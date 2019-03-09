# -*- coding: utf-8 -*-
"""
Created on Fri Sep 07 10:45:29 2018

@author: gao->ilvcr
"""

__author__ = 'gao->ilvcr'


pathsource = 'C:\\Users\\Administrator\\Desktop\\addoneonacolresult.txt'

def addoneonacol():
    reqlist = []
    with open(pathsource, 'w+') as sor:
        for beforeadd in range(4095, 5017):
            reqlist.append(beforeadd)
            #print reqlist       
        
        for data in reqlist:
            #print data            
            sor.write(str(data)+'\n')
                       
if __name__ == '__main__':
    addoneonacol()
    
    