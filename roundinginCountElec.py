# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:46:33 2018

@author: gao->ilvcr
Description: 统计电荷布局数时对书籍进行的四舍五入(保留二位有效数字,两位为0则为三位)
"""

__author__ = 'gao->ilvcr'

pathsource = 'C:\\Users\\Administrator\\Desktop\\roundinginCountElec.txt'
pathresult = 'C:\\Users\\Administrator\\Desktop\\roundinginCountElecResult.txt'

def roundinginCountElec():
    with open(pathsource, 'rb') as sor:
        with open(pathresult, 'w') as rel:
            for line in sor.readlines():
                linea = line.strip().split()
                #print linea
                lineb = [str(i) for i in linea]
                roundtwo = str(round(float(lineb[2]),2))
                #print roundtwo
                roundthree = str(round(float(lineb[2]),3))
                #print roundthree
                
                linec = lineb[0]+'\t'+lineb[1]+'\t'+roundtwo+'\t'+roundthree
                #print linec.strip().split()
                lined = linec.strip().split()
                linee = [str(i) for i in lined]
                #print linee
                if float(linee[2]) == 0:
                    linef = linee[0]+'\t'+linee[1]+'\t'+linee[3]
                else:
                    linef = linee[0]+'\t'+linee[1]+'\t'+linee[2]
                #print linef
                rel.writelines(linef+'\n')


if __name__ == '__main__':
    roundinginCountElec()
