#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: gauss_fitting.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Mon Feb  21 15:24:52 2017
# Description: 实现高斯多峰拟合
#************************************************************************#

from scipy.optimize import curve_fit


#三高斯拟合
def func3(x,a1,a2,a3,m1,m2,m3,s1,s2,s3):

    return a1*np.exp(-((x-m1)/s1)**2)+a2*np.exp(-((x-m2)/s2)**2)+a3*np.exp(-((x-m3)/s3)**2)


#限制参数，bounds代表参数上下限，参数即为def func3里面x后的所有参数
popt, pcov = curve_fit(func3, x, y, bounds=([y0,y0,y0,-5000,-1000,500,1200,1200,1200], [y_max,y_max,y_max,-500,1000,5000,30000,30000,30000]))




'''
import numpy as np  
import pylab as plt  
#import matplotlib.pyplot as plt  
from scipy.optimize import curve_fit  
from scipy import asarray as ar,exp  
   
x = ar(range(10))  
y = ar([0,1,2,3,4,5,4,3,2,1])  
   
   
def gaussian(x,*param):  
    return param[0]*np.exp(-np.power(x - param[2], 2.) / (2 * np.power(param[4], 2.)))+param[1]*np.exp(-np.power(x - param[3], 2.) / (2 * np.power(param[5], 2.)))  
   
   
popt,pcov = curve_fit(gaussian,x,y,p0=[3,4,3,6,1,1])  
print popt  
print pcov  
   
plt.plot(x,y,'b+:',label='data')  
plt.plot(x,gaussian(x,*popt),'ro:',label='fit')  
plt.legend()  
plt.show()
'''
