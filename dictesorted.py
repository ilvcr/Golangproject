# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:04:52 2018

@author: gao->ilvcr
Description: 模拟后统计键长键级并进行排序
"""

__author__ = 'gao->ilvcr'

pathsource = 'C:\\Users\\Administrator\\Desktop\\tuplesorted.txt'
pathresult = 'C:\\Users\\Administrator\\Desktop\\tuplesortedResult.txt'

import json

def setsorted():
    with open(pathsource, 'rb') as sor:
        with open(pathresult, 'w') as rel:
            for line in sor.readlines():
                linea = line.strip().split()
                #print linea                
                dic = {}
                keys = []
                dic[linea[0]] = linea[1]
                keys.append(linea[0])
                #print dic
                for k in keys:
                    lined = k+':'+dic[k]+'\n'
                    #linee = sorted(lined.iteritems(), key=lambda d:d[1]['val'], reverse = True)
                    #linee = json.loads(lined)
                    #linef = sorted(zip(linee.values(), linee.keys()))                    
                    #print linef
                    #rel.write(k+':'+dic[k]+'\n')
                

if __name__ == '__main__':
    setsorted()