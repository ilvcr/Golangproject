# -*- coding: utf-8 -*-
"""
Created on Wed Aug 08 11:16:35 2018

@author: gao->ilvcr
"""

__author__ = 'gao->ilvcr'


'''
   PIL读取并显示图片
'''


import numpy as np
from PIL import Image


#1. 显示图片
im = Image.open('lena.png')
im.show()

#2. 将 PIL Image 图片转换为 numpy 数组
im_array = np.array(im)
# 也可以用 np.asarray(im) 区别是 np.array() 是深拷贝，np.asarray() 是浅拷贝

#3. 直接调用 Image 类的 save 方法保存 PIL 图片
from PIL import Image
I = Image.open('lena.png')
I.save('new_lena.png')

#4. 将 numpy 数组转换为 PIL 图片
import matplotlib.image as mpimg
from PIL import Image
lena = mpimg.imread('lena.png') # 这里读入的数据是 float32 型的，范围是0-1
im = Image.fromarray(np.uinit8(lena*255))
im.show()

#5. RGB 转换为灰度图
from PIL import Image
I = Image.open('lena.png')
I.show()
L = I.convert('L')
L.show()

