# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:11:27 2018

@author: gao->ilvcr
Description: 模拟后统计CON之间的键长(保留四位有效数字)
"""

__author__ = 'gao->ilvcr'

pathsource = 'C:\\Users\\Administrator\\Desktop\\countlength.txt'
pathresult = 'C:\\Users\\Administrator\\Desktop\\countlengthResult.txt'

def countLength():
    with open(pathsource, 'rb') as sor:
        with open(pathresult, 'w') as rel:
            for line in sor.readlines():
                linea = line.strip().split()
                lineb = [str(i) for i in linea]
                #print lineb[1]+lineb[0]+'-'+lineb[1]+lineb[-3]+"\t"+lineb[2]
                if lineb[0] == 1:
                    break
                else:
                    linec = lineb[1]+lineb[0]+'-'+lineb[1]+lineb[-3]+"\t\t"+lineb[2]
                    #print linec
                    rel.writelines(linec+'\n')#'"'+line[:s]+'"'+","
            
if __name__ == '__main__':
    countLength()    