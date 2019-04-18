#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_to_data.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  3 10:43:47 2018
# Description: 将图片读取为数据
#************************************************************************#

import numpy as np

class imageToData(object):
    '''
        将图片读取为数据的类
    '''
    def __init__(self):
        pass

    def pil_image2numpy_array(self, im):
        '''
            使用PIL Image将图片转换为便于处理的numpy数组
        '''
        im_array = np.array(im)

        return im_array





