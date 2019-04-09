#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_cutting.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Fri  19 15:24:52 2017
# Description: 图像切割, 滑动切割,固定切割
#************************************************************************#

from PIL import Image

class imageCutting(object):
    '''
        图像切割
    '''
    def __init__(self):
        pass

    def image_cutting_slide(self, idxy, vx, vy):
        '''
            滑动切割图片, 修改图片idxy
            param: idxy为图片id的后两位
            param: vx, vy
        '''

        #打开图片
        name_01 = 'sample' + self.idxy + '.jpg'
        name_02 = 'sample' + self.idxy + '_cut_'
        im = Image.open(name_01)

        #偏移量
        dx = 40
        dy = 40
        n = 1

        #切割左上角
        x1 = 0
        y1 = 0
        x2 = self.vx
        y2 = self.vy


        #纵向切
        while  x2 <= 320:
            #横向切
            while y2 <= 480:
                name_03 = name_02 + str(n) + '.jpg'
                im_02 = im.crop((y1, x1, y2, x2))
                im2.save(name_03)
                y1 = y1 + dy
                y2 = y1 + self.vy
                n = n + 1

            x1 = x1 + dx
            x2 = x1 + self.vx
            y1 = 0
            y2 = vy

        print "Image cutted success, cutted's image is : "

        return n-1

    def image_cutting_mean(self, im):
        '''
            等分切割图片, 
        '''
        #图片的宽度和高度
        image_size = self.im.size
        print "图片的宽度和高度分别是 : {}".format(image_size)
        
        xx = 3
        yy = 2
        x = img_size[0] // xx
        y = img_size[1] // yy

        for i in range(yy):
            for j in range(xx):
                left = i * x
                up = y * j
                right = left + x
                low = up + y
                
                region = self.im.crop((left, up, right, low))
                print "left : {}, up : {}, right : {}, low : {}\n".format(left, up, right, low)
                temp = str(i) + str(j)
                region.save(savepath+temp+'.png')


    def image_cutting_fixed_point(self, im):
        '''
            定点切割图像, 
            param: im为使用Image.open()打开的图片对象
        '''

        #图片的宽度和高度
        image_size = self.im.size
        print "图片的宽度和高度分别是 : {}".format(image_size)

        left = 80
        upper = 210
        right = 505
        lower = 640

        region = self.im.crop((left, upper, right, lower))
        region.save(savepath)

        return region

