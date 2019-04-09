#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_edge_detection.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Mon Feb  13 10:28:52 2017
# Description: 边缘检测
#************************************************************************#

import cv2

class edgeDetection(object):
    '''
        边缘检测
    '''
    def __init__(self):
        pass

    def edge_direction_canny(self, im):
        '''
            Canny边缘检测
        '''
        #im = cv2.imread("example")
        cv2.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
        cv2.imshow('input_image', self.im
                   )
        blurred = cv2.GaussianBlur(self.im, (3, 3), 0)
        gray = cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY)

        #xgrad = cv2.Sobel(gray, cv.CV_16SC1, 1, 0) #x方向梯度
        #ygrad = cv2.Sobel(gray, cv.CV_16SC1, 0, 1) #y方向梯度
        #edge_output = cv2.Canny(xgrad, ygrad, 50, 150)
        #上三行与下一行等价！
        
        edge_output = cv2.Canny(gray, 50, 150)
        cv2.imshow("Canny Edge", edge_output)

        dst = cv2.bitwise_and(self.im, self.im, mask= edge_output)
        cv2.imshow("Color Edge", dst)

        cv.waitKey(0)
        cv.destroyAllWindows()

        return blurred, gray, xgrad, ygrad, edge_output, dst

    
    def 


        
        
