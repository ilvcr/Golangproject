#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: save_image.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Jun  19 10:23:32 2018
# Description: 保存图像
#************************************************************************#


class saveImage(object):
    '''
        保存图像的类
    '''
    def __init__(self):
        pass

    def save_image_using_Image(self, im):
        '''
            调用Image中的save方法保存PIL图片
        '''
        im = im.save()
        
        return im

    def save_image_using_plt(self, im):
        '''
            保存matplotlib画出的图像
            适用于保存任何matplorlib画出的图像, 相当于一个screencapture
        '''
        plt.imshow(im)
        plt.axis('off')

        plt.savefig(save_path, format='png', transparent=True, dpi=300, pad_inches=0)


    def save_image_using_array(self, im):
        '''
            将array保存为图像
        '''
        misc.imsave(save_path+'new_sample_size.png', im)

    def direct_save_image_using_array(self, im):
        '''
            直接保存array, 此方法不会对图像质量造成损失
        '''
        np.save('new_sample_size', im) #自动在文件名后加上.npy

        img = np.load('new_sample_size.npy') #读取前面保存的数组

    
