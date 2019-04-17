#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_equalization.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Wed Nov  29 12:41:09 2017
# Description: 对图像进行均衡化处理
#************************************************************************#


from skimage import data, exposure
import matplotlib.pyplot as plt

class imageEqualization(object):
    '''
        对图像进行均衡化处理
    '''
    def __init__(self):
        pass

    def image_equalization_process(self, im):
        '''
            均衡化处理
        '''
        #im = data.moon()
        #plt.figure("hist", figsize=(8, 8))

        im_arr = im.flatten()

        plt.subplot(221)
        plt.imshow(im, plt.cm.gray) #原始图像

        plt.subplot(222)
        plt.hiast(im_arr, bins=256, normed=1, edgecolor='None', facecolor='red') #原始图像直方图

        im_01 = exposure.equalize_hist(im)
        im_arr_01 = im_01.flatten()

        plt.subplot(223)
        plt.imshow(im_01, plt.cm.gray) #均衡化图像

        plt.subplot(224)
        plt.hiast(im_arr_01, bins=256, normed=1, edgecolor='None', facecolor='red') #均衡化图像直方图
        
        plt.show()

        return im, im_arr, im_01, im_arr_01




