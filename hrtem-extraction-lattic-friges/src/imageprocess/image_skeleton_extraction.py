#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_skeleton_extraction.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 11:00:24 2019
# Description: Skeleton extraction  骨架提取
#************************************************************************#

from skimage import morphology, draw, feature, color, data, filter
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

class skeletonExtraction(object):
    '''
        骨架提取, 二值图像细化
        将一个连通区域细化成一个像素的宽度，用于特征提取和目标拓扑表示
    '''

    def __init__(self):
        pass

    def skeleton_extraction_morphology(self, im):
        '''
            使用morphology中的Skeletonize（）函数。
            函数原型：
                skimage.morphology.skeletonize(image)
        '''
        #实施骨架算法
        skleton = morphology.skeletonize(self.im)

        #显示结果
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

        ax1.imshow(self.im, cmap=plt.cm.gray)
        ax1.axis('off')
        ax1.set_title('original', fontsize=20)

        ax2.imshow(skeleton, cmap=plt.cm.gray)
        ax2.axis('off')
        ax2.set_title('skeleton', fontsize=20)

        fig.tight_layout()
        plt.show()

        return im, sklenton


    def skeleton_extraction_medial_axis(self, im):
        '''
            medial_axis利用中轴变换方法计算前景(1值)目标对象的宽度,
            函数原型:
            skimage.morphology.medial_axis(image, mask=None, return_distance=False)
                mask:掩模. 默认为None, 如果给定一个掩模,
                        则在掩模内的像素值才执行骨架算法.
                return_distance: bool型值，默认为False.
                        如果为True, 则除了返回骨架, 还将距离变换值也同时返回.
                        这里的距离指的是中轴线上的所有点与背景点的距离.
        '''

        #计算中轴和距离变换值
        skel, distance =morphology.medial_axis(self.im, return_distance=True)

        #中轴上的点到背景像素点的距离
        dist_on_skel = distance * skel

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
        ax1.imshow(data, cmap=plt.cm.gray, interpolation='nearest')

        #用光谱色显示中轴
        ax2.imshow(dist_on_skel, cmap=plt.cm.spectral, interpolation='nearest')
        ax2.contour(self.im, [0.5], colors='w')  #显示轮廓线

        fig.tight_layout()
        plt.show()

        return skel, distance, dist_on_skel
        
    def watershed_algorithm(self, im):
        '''
            分水岭算法是一种用于图像分割的经典算法，是基于拓扑理论的数学形态学的分割方法。
            如果图像中的目标物体是连在一起的，则分割起来会更困难，分水岭算法经常用于处理此类问题，通常会取得比较好的效果。

            分水岭算法可以和距离变换结合，寻找“汇水盆地”和“分水岭界限”，从而对图像进行分割。
            二值图像的距离变换就是每一个像素点到最近非零值像素点的距离，可使用scipy包来计算距离变换。
        '''

        #使用分水岭算法
        distance = ndi.distance_transform_edt(self.im) #距离变换

        local_maxi =feature.peak_local_max(distance, indices=False,
                                           footprint=np.ones((3, 3)),
                                           labels=image)   #寻找峰值

        markers = ndi.label(local_maxi)[0] #初始标记点
        labels =morphology.watershed(-distance, markers, mask=image) #基于距离变换的分水岭算法

        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
        axes = axes.ravel()
        ax0, ax1, ax2, ax3 = axes

        ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
        ax0.set_title("Original")

        ax1.imshow(-distance, cmap=plt.cm.jet, interpolation='nearest')
        ax1.set_title("Distance")

        ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
        ax2.set_title("Markers")

        ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
        ax3.set_title("Segmented")

        for ax in axes:
            ax.axis('off')

        fig.tight_layout()
        plt.show()

        return distance, local_maxi, markers, labels

    
    def watershed_algorithm_basedon_gradient(self, im):
        '''
            基于梯度的分水岭算法
        '''
        #image =color.rgb2gray(data.camera())
        denoised = filter.rank.median(self.im, morphology.disk(2)) #过滤噪声

        #将梯度值低于10的作为开始标记点
        markers = filter.rank.gradient(denoised, morphology.disk(5)) <10
        markers = ndi.label(markers)[0]

        gradient = filter.rank.gradient(denoised, morphology.disk(2)) #计算梯度
        labels =morphology.watershed(gradient, markers, mask=image) #基于梯度的分水岭算法

        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
        axes = axes.ravel()
        ax0, ax1, ax2, ax3 = axes

        ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
        ax0.set_title("Original")

        ax1.imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
        ax1.set_title("Gradient")

        ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
        ax2.set_title("Markers")

        ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
        ax3.set_title("Segmented")

        for ax in axes:
            ax.axis('off')

        fig.tight_layout()
        plt.show()

        return denoised, gradient, labels


