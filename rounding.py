# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:10:27 2018

@author: gao->ilvcr
Description: 四舍五入，保留二位有效数字,n为列数
"""

__author__ = 'gao->ilvcr'

pathsource = 'C:\\Users\\Administrator\\Desktop\\countlengthResult.txt'
pathresult = 'C:\\Users\\Administrator\\Desktop\\rounding.txt'

def rounding(n):
    with open(pathsource, 'rb') as sor:
        with open(pathresult, 'w') as rel:
            for line in sor.readlines():
                linea = line.strip().split()
                lineb = [str(i) for i in linea]
                linec = float(lineb[n-1])
                #print float('%.2f' % linec)
                #lined = lineb[0]+"\t\t"+str(float('%.2f' % linec))
                lined = lineb[0]+"\t\t"+str(round(float(linec),2))
                #print lined
                rel.writelines(lined+'\n')#'"'+line[:s]+'"'+","                
            
if __name__ == '__main__':
    rounding(2)    