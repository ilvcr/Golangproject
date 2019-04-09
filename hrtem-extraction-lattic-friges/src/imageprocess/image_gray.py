#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_gray.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 12:25:47 2019
# Description: 对图像进行灰度化处理
#************************************************************************#

import copy
import math

class imageGray(object):
    '''
        对图像进行灰度化处理
    '''
    def __init__(self):
        pass

    def image_to_gray_process(self, im):
        '''
            读入正常图像数据并对其进行灰度化处理
        '''
        
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        return im_gray

    def gray_image_to_two_valued_handle(self, im):
        '''
            对灰度图像进行二值化处理
        '''

        #二值化处理
        im_ret, im_fixed = cv2.threshold(self.im, 50, 255, cv2.THRESH_BINARY)

        return im_ret, im_fixed

    def gray_image_to_gamma_process(self, im):
        '''
            对灰度图像进行伽马变换
        '''

        #伽马变换
        im_gamma = copy.deepcopy(self.im)
        
        rows = self.im.shape[0]
        cols = self.im.shape[1]
        for i in range(rows):
            for j in range(cols):
                im_gamma[i][j] = 3*math.pow(im_gamma[i][j], 0.8)

        return self.im, im_gamma

    def gray_image_to_log_process(self, im):
        '''
            对灰度图像进行对数变换
        '''
        
        #对数变换
        im_logc = copy.deepcopy(self.im)

        rows = self.im.shape[0]
        cols = self.im.shape[1]
        for i in range(rows):
            for j in range(cols):
                im_logc[i][j] = 3*math.log(1 + im_logc[i][j])

        return self.im, im_logc

    def gray_image_to_cover_process(self, im):
        '''
            对灰度图像进行反色变换
        '''

        #补色变换
        im_cover = copy.deepcopy(self.im)

        rows = self.im.shape[0]
        cols = self.im.shape[1]
        for i in range(rows):
            for j in range(cols):
                im_cover[i][j] = 255 - im_cover[i][j]
   
        return self.im, im_cover

