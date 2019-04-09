#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_preprocess.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Mon Jul  16 10:00:28 2018
# Description: 
#************************************************************************#

from PIL import Image
import matplotlib.image as mpimg

def image_preprocess():
    '''
        获取图像的读取路径及保存路径
    '''
    read_path = raw_input("请输入图像读取路径及图像名称: ")
    save_path = raw_input("请输入图像的保存路径: ")

    im_using_pil = Image.open(read_path)

    im_using_mpimg = mpimg.imread(read_path)
