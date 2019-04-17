#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_process.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thur Jun  7 12:52:39 2018
# Description: 图像处理
#************************************************************************#

class imageProcess(object):
    '''
        图像处理如：
            增加噪声
            RGB图转换为灰度图
            使用scipy对图片进行缩放
    '''
    def __init__(self):
        pass

    def add_noise_in_image(self, im):
        '''
            为图像增加噪声
        '''

        #读取噪声
        #im = cv2.imread(read_path, cv2.IMREAD_UNCHANGED)
        rows, cols, _ = im.shape

        #增加噪声
        for i in range(5000):
            x = np.random.randint(0, rows)
            y = np.random.randint(0, clos)
            im[x, y, :] = 255

        cv2.imshow("noise", im)
        
        #等待显示
        cv2.waitKey(0)
        cv2.destoryAllWIndows()

        return im


    def RGB_to_gray_image(self, im):
        '''
            RGB图转换为灰度图
        '''
        im.show()

        im_gray = im.covert('gray')
        im_gray.show()

        return im_gray

    def using_scipy_resize_image(self, im):
        '''
            使用scipy对图像进行缩放
        '''
        im_new_size = misc.imresize(im, 0.5)
        # 第二个参数若大于1, 则为放大; 小于1则为缩小.
        
        plt.imshow(im_new_size)

        plt.axis('off')
        plt.show()

        return im_new_size


