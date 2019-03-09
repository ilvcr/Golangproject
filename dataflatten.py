# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:32:54 2018

@author: gao->ilvcr
Description: 统计电荷布局数时数据扁平化处理
"""

__author__ = 'gao->ilvcr'


pathsource = 'C:\\Users\\Administrator\\Desktop\\dataflatten.txt'
pathresult = 'C:\\Users\\Administrator\\Desktop\\dataflattenResult.txt'

def dataflatten():
    with open(pathsource, 'rb') as sor:
        with open(pathresult, 'w') as rel:
            for line in sor.readlines():
                linea = line.strip().split()
                #print linea
                lineb = [str(i) for i in linea]
                #print lineb[1]+'\t'+lineb[2]+'\n'+lineb[4]+'\t'+lineb[5]
                #rounding str(round(float(linec),2))
                roundtwoinsecond = str(round(float(lineb[2]),2))
                roundtwoinfifth = str(round(float(lineb[5]),2))
                #print roundtwo
                #roundthreeinsecond = str(round(float(lineb[2]),3))
                #roundthreeinfifth = str(round(float(lineb[5]),2))
                
                linec = lineb[0]+'\t'+lineb[1]+'\t'+lineb[2]+'\t'+roundtwoinsecond+'\n'+ \
                        lineb[3]+'\t'+lineb[4]+'\t'+lineb[5]+'\t'+roundtwoinfifth    
                #print linec
                lined = linec.strip().split()
                linee = [str(i) for i in lined]
                #print linee
                if float(linee[3]) == 0 or float(linee[7]) == 0:
                    linef = linee[0]+'\t'+linee[1]+'\t'+linee[2]+'\n'+\
                            linee[4]+'\t'+linee[5]+'\t'+linee[6]
                else:
                    linef = linee[0]+'\t'+linee[1]+'\t'+linee[3]+'\n'+\
                            linee[4]+'\t'+linee[5]+'\t'+linee[7]
                #print linef
                rel.writelines(linef+'\n')
                
                
if __name__ == '__main__':
    dataflatten()