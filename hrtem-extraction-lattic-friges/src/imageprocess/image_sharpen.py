#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_sharpen.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 12:06:52 2019
# Description: 图像锐化处理
#************************************************************************#


class imageSharpen(object):
    '''
        图像锐化操作
    '''
    
    def __init__(self):
        pass

    def kernel_sharpen_01(self, im):
        '''
            第一个卷积核
        '''
        kernel_sharpen_01 = np.array([
            [-1, -1, -1],
            [-1, 9, -1],
            [-1, -1, -1]])

        #卷积计算
        im_01 = cv2.filter(self.im, -1, kernel_sharpen_01)

        #显示锐化效果
        cv2.imshow("Original Image", self.im)
        cv2.imshow("sharpen_01 Image", im_01)
        
        #停顿
        if cv2.waitKey(0) & 0xFF == 27:
            cv2.destoryAllWindows()

        return self.im, im_01

    def kernel_sharpen_02(self, im):
        '''
            第二个卷积核
        '''
        kernel_sharpen_02 = np.array([
            [1, 1, 1],
            [1, -7, 1],
            [1, 1, 1]])

        #卷积计算
        im_02 = cv2.filter(self.im, -1, kernel_sharpen_02)

        #显示锐化效果
        cv2.imshow("Original Image", self.im)
        cv2.imshow("sharpen_02 Image", im_02)
        
        #停顿
        if cv2.waitKey(0) & 0xFF == 27:
            cv2.destoryAllWindows()

        return self.im, im_02
        
    def kernel_sharpen_03(self, im):
        '''
            第三个卷积核
        '''
        kernel_sharpen_03 = np.array([
            [-1, -1, -1, -1, -1],
            [-1, 2, 2, 2, -1],
            [-1, 2, 8, 2, -1],
            [-1, 2, 2, 2, -1],
            [-1, -1, -1, -1, -1]]) / 8.0

        #卷积计算
        im_03 = cv2.filter(self.im, -1, kernel_sharpen_03)
        
        #显示锐化效果
        cv2.imshow("Original Image", self.im)
        cv2.imshow("sharpen_02 Image", im_03)
        
        #停顿
        if cv2.waitKey(0) & 0xFF == 27:
            cv2.destoryAllWindows()
       
        return self.im, im_03

    def kernel_sharpen_04(self, im):
        '''
            第四个卷积核、锐化通用卷积核
        '''
        kernel_sharpen_04 = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]])

        #卷积计算
        im_04 = cv2.filter(self.im, -1, kernel_sharpen_03)

        #显示锐化效果
        cv2.imshow("Original Image", self.im)
        cv2.imshow("sharpen_02 Image", im_04)

        #停顿
        if cv2.waitKey(0) & 0xFF == 27:
            cv2.destoryAllWindows()
        
        return self.im, im_04
        
        




