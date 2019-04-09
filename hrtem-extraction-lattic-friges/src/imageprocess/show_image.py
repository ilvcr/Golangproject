#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: show_image.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  28 11:25:39 2017
# Description: 显示图像的类
#************************************************************************#

import image_preprocess
from PIL import Image
import matplotlib.image as mping # mping用于读取图片

class showImage(object):
    '''
        使用Image方法与mping显示图片
    '''
    def __init__(self):
        pass

    def show_image_using_pil(self, im):
        '''
            显示图片
            im为使用Image.open("sample")打开的图片
        '''
        self.im.show()

        #return self.im

    def show_image_using_mping(self, im):
        '''
            显示图片
            im为使用 mping.imread('sample')打开的图片
        '''

        #im 为一个np.array数组, 可对其进行任意处理
        self.im.shape(512, 512, 3)

        plt.imshow(self.im) # 显示图片
        plt.axis('off') # 不显示坐标轴
        plt.show()
    
        #return self.im

    
    def show_image_using_plt(self, im):
        '''
            使用plt显示图片
        '''
        np.save('sample', self.im)
        img = np.load('sample.npy')

        plt.imshow(img)
        plt.axis('off')
        plt.show()

    def show_onething_channel_inimage(self, im):
        '''
            显示图片的e第一个通道
        '''
        im_1 = self.im[:, :, 0]
        plt.imshow('im_1')
        plt.show()

        return im_1

    def numpy_array_to_pil_image(self, im):
        '''
            将numpy数组转换为PIL图片
        '''
        im = Image.formarray(np.uinit8(im*255))

        im.show()




