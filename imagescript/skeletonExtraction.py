# -*- coding: utf-8 -*-
"""
Created on Wed Aug 08 10:52:23 2018

@author: gao->ilvcr
"""

__author__ = 'gao->ilvcr'


'''
    Skeleton extraction
    骨架提取
'''

import cv
from PIL import Image

#图像存储路径
IMAGEPATH = r'C:\Users\Administrator\Desktop\图像处理脚本'#假设路径为C:\Users\Administrator\Desktop\图像处理脚本


#读取上一步操作的图像
array = Image.open(IMAGEPATH)

def Thin(image,array):
    h = image.height
    w = image.width
    iThin = cv.CreateImage(cv.GetSize(image),8,1)
    cv.Copy(image,iThin)
    for i in range(h):
        for j in range(w):
            if image[i,j] == 0:
                a = [1]*9
                for k in range(3):
                    for l in range(3):
                        if -1<(i-1+k)<h and -1<(j-1+l)<w and iThin[i-1+k,j-1+l]==0:
                            a[k*3+l] = 0
                sum = a[0]*1+a[1]*2+a[2]*4+a[3]*8+a[5]*16+a[6]*32+a[7]*64+a[8]*128
                iThin[i,j] = array[sum]*255
    return iThin        
    
def Two(image):
    w = image.width
    h = image.height
    size = (w,h)
    iTwo = cv.CreateImage(size,8,1)
    for i in range(h):
        for j in range(w):
            iTwo[i,j] = 0 if image[i,j] < 200 else 255
    return iTwo
    
image = cv.LoadImage('pic3.jpg',0)
iTwo = Two(image)
iThin = Thin(iTwo,array)
cv.ShowImage('image',image)
cv.ShowImage('iTwo',iTwo)
cv.ShowImage('iThin',iThin)
cv.WaitKey(0)