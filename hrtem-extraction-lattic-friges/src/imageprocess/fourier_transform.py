#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: fourier_transform.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Mon May  4 11:01:44 2018
# Description: 傅里叶变换及反傅里叶变换
#************************************************************************#

from src.imageprocess import image_to_data
import matplotlib.pyplot as plt
from numpy as np
import cv2

class imageFFT(object):
    '''
        傅里叶变换及反傅里叶变换
    '''
    def __init__(self):
        pass

    def image_fft_using_formula(self, im):
        '''
            使用公式的傅里叶变换
        '''

        # 由公式转换为灰度图
        im = 0.2126 * im[:, :, 0] + 0.7152 * im[:, :, 1] + 0.0722 * im[:, :, 2]

        #显示原图
        plt.subplot(231)
        plt.imshow(im, 'gray')
        plt.title('orginal')

        #进行傅里叶变换, 并显示结果
        fft2 = np.fft.fft2(im)
        plt.subplot(232)
        plt.imshow(np.abs(fft2), 'gray')
        plt.title('fft2')

        #将图像变换的原点移动到频域矩形的中心, 并显示效果
        shift_to_center = np.fft.fftshift(fft2)
        plt.subplot(233)
        plt.imshow(np.abs(shift_to_center), 'gray')
        plt.title('shift_to_center')

        #对傅里叶变换的结果进行对数变换, 并显示效果
        log_fft2 = np.log(1+np.abs(fft2))
        plt.subplot(235)
        plt.imshow(log_fft2, 'gray')
        plt.title('log.fft2')

        #对中心化后的结果进行对数变换, 并显示效果
        log_shift_to_center = np.log(1+np.abs(shift_to_center))
        plt.subplot(236)
        plt.imshow(log_shift_to_center, 'gray')
        plt.title('log_shift_to_center')

        return im, fft2, shift_to_center, log_fft2, log_shift_to_center

    def image_fft_using_cv2(self, im):
        '''
            使用cv2库进行图像的傅里叶变换
        '''
        #im = cv2.imread(read_path, 0)

        dft = cv2.dft(np.float32(im), flags=cv2.DFT_COMPLEX_OUTPUT)

        plt.subplot(211)
        plt.axis('off')
        plt.title('dft')
        plt.imshow(20*np.log(cv2.magnitude(dft[:, :, 0], dft[:, :, 1])), cmap='gray')

        dft_shift = np.fft.fftshift(dft)
        plt.subplot(212)
        plt.axis('off')
        plt.title('def_shift')
        plt.imshow(20*np.log(cv2.magnitude(def_shift[:, :, 0], dft_shift[:, :, 1])), cmap='gray')

        return dft, dft_shift

    def image_ifft_using_cv2(self, im):
        '''
            使用cv2库进行图像的反傅里叶变换
        '''
        idft_shift = np.fft.ifftshift(im)
        plt.subplot(211)
        plt.axis('off')
        plt.title('origin')
        plt.imshow(idft_shift, cmap='gray')

        idft = cv2.idft(idft_shift)
        plt.subplot(212)
        plt.axis('off')
        plt.title('idft_shift')
        plt.imshow(cv2.magnitude(idft[:, :, 0], idft[:, :, 1]), cmap='gray')

        plt.show()

        return idft_shift, idft


        

