#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_filter_process.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 11:36:15 2019
# Description: 
#************************************************************************#

def mean_filter_image(im):
    '''
        调用OpenCV实现均值滤波
        函数原型:result = cv2.blur(原始图像,核大小)
        其中:
            核大小是以（宽度，高度）表示的元祖形式;
            常见的形式包括:核大小（3, 3）和（5, 5）
    '''
    #img = cv2.imread('test01.png')
    source = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    # 均值滤波
    result = cv2.blur(source, (5, 5))

    # 显示图形
    titles = ['Source Image', 'Blur Image'] 
    image = [source, result] 
    for i in xrange(2): 
        plt.subplot(1,2,i+1)
        plt.imshow(images[i], 'gray') 
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([]) 
    
    plt.show() 
    
    return image
  
def box_filter_image(im):
    '''
        调用OpenCV实现方框滤波
        函数原型:result = cv2.boxFilter(原始图像, 目标图像深度, 核大小, normalize属性)
        其中:
            目标图像深度是int类型;通常用“-1”表示与原始图像一直;
            核大小主要包括（3;3）和（5;5）
    '''
    source = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    
    #方框滤波 
    result = cv2.boxFilter(source, -1, (5,5), normalize=1) 
    
    #显示图形 
    titles = ['Source Image', 'BoxFilter Image'] 
    image = [source, result] 
    
    for i in xrange(2): 
        plt.subplot(1,2,i+1)
        plt.imshow(images[i], 'gray') 
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([])
    
    plt.show() 
    
    return image
    
def gaussian_blur_filter_image(im):
    '''
        调用OpenCV实现高斯滤波
        函数原型：dst = cv2.GaussianBlur(src, ksize, sigmaX)
        其中,
            目标图像深度是int类型, 通常用“-1”表示与原始图像一直;
            核大小主要包括（3, 3）和（5, 5）
    '''
    source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    
    #高斯滤波 
    result = cv2.GaussianBlur(source, (3,3), 0) 
    
    #显示图形 
    titles = ['Source Image', 'GaussianBlur Image'] 
    image = [source, result] 
    
    for i in xrange(2): 
        plt.subplot(1,2,i+1)
        plt.imshow(images[i], 'gray') 
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([]) 
    
    plt.show() 
    
    return image
    
def median_blur_filter_image(im):
    '''
        调用OpenCV实现中值滤波
        函数原型：dst = cv2.medianBlur(src, ksize)
        其中:
            src表示源文件,ksize表示核大小;
            核必须是大于1的奇数, 如3、5、7等
    '''
    #读取图片 
    #img = cv2.imread('test01.png') 
    
    #中值滤波 
    result = cv2.medianBlur(img, 3) 
    
    #显示图像 
    cv2.imshow("source img", img) 
    cv2.imshow("medianBlur", result) 
    
    #等待显示 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    
    return result
