#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_date_extended_set.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 13:05:24 2019
# Description: 扩充图像数据集的方法
#************************************************************************#

import os
import time
from PIL import Image
import matplotlib.pyplot as plt
from diagnose_logging import Logger

#声明日志
log = Logger('image_date_extended_set')
logger = log.getlog()

class imageDataExtendedSet(object):
    '''
        扩充图像数据集
    '''
    def __init__(self, rootPath, export_path_base):
        
        self.rootPath = rootPath #图像完整路径
        self.export_path_base = export_path_base
        
        #创建根目录
        try:
            if not in os.path.exists(export_path_base):
                os.mkdir(export_path_base)
        except Exception as e:
            logger.error(e)

        logger.info('image_date_extended_set: %s', rootPath)

    def get_savename(self, operate):
        '''
            :param  export_path_base: 图像输出路径
            :param  operate: 图像区域名

            :return: 返回图像存储名
        '''

        try:
            #获取时间戳， 用于区分图像
            now = time.time()
            tail_time = str(round(now * 1000000))[-4:] #时间戳尾数

            head_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            #时间标签
            label = str(head_time + tail_time)


            #输出文件夹
            export_path_base = self.export_path_base
            #子文件夹以"操作operate"命名
            out_path = export_path_base + operate
            #创建子文件夹
            if not os.path.exists(out_path):
                os.mkdir(out_path)

            #存储完整路径
            save_name = outpath + '/' + operate + '_' + label + '.jpg'

            #日志
            logger.info('save: %s', save_name)
            return save_name
        
        except Exception as e:
            logger.error('get_savename ERROR')
            logger.error(e)

    def lightness(self, light):
        '''
            改变图像亮度
            推荐值: 0.87, 1.07
            明亮程度:
                darker < 1.0 < lighter
        '''

        try:
            operate = 'lightness_' + str(light)
            
            #完整图像路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                #图像左右翻转
                out = image.point(lambda p: p*light)
                #重命名
                save_name = self.get_savename(operate)
                #图像存储
                out.save(save_name)

        #日志
        #logger.info(operate)
        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)


    def rotate(self, angle):
        '''
            图像旋转15°、30°
        '''

        try:
            operate = 'rotate_' + str(angle)
            
            #图像完整路径
            root_path = self.rootPath

            with Image.open(rootPath) as image:
                #图像左右翻转
                out = image.rotate(angle)
                #重命名
                save_name = self.get_savename(operate)
                #图像存储
                out.save(save_name, quality=100)

        #日志
        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)

    def transpose(self):
        '''
            图像左右翻转操作
        '''

        try:
            operate = 'transpose'
            #图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                #图像左右翻转
                out = image.transpose(Image.FLIP_LEFT_RIGHT)
                #重命名
                save_name = self.get_savename(operate)
                #图像存储
                out.save(save_name, quality=100)
        #日志
        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)

    def deform(self):
        '''
            图像拉伸
        '''

        try:
            operate = 'deform'
            #图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                w, h = image.size
                w = int(w)
                h = int(h)

                #拉伸成宽为w的正方形
                out_ww = image.resize((int(w), int(w)))
                save_name = self.get_savename(operate + '_ww')
                out.ww.save(save_name, quality=100)
                #拉伸为宽为h的正方形
                out_ww = image.resize((int(h), int(h)))
                save_name = self.get_savename(operate + '_hh')
                out_ww.save(save_name, quality=100)

        #日志
        except Exception as e:
            logger.error('ERROR %s', operate)
            logger.error(e)

    def crop(self):
        '''
            提取四个角落和中心区域
        '''

        try:
            operate = 'crop'
            #图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as Image:
                w, h = image.size
                
                #切割后尺寸
                scale = 0.875
                
                #切割后长宽
                ww = int(w * scale)
                hh = int(h * sacle)
                
                #图像起点， 左上角坐标
                x = y =0

                #切割左上角
                x_lu = x
                y_lu = y
                out_lu = image.crop((x_lu, y_lu, ww, hh))
                save_name = self.get_savename(operate + '_lu')
                out_lu.save(save_name, quality=100)

                #切割左下角
                x_ld = int(x)
                y_ld = int(y + (h - hh))
                out_ld = image.crop((x_ld, y_ld, ww, hh))
                save_name = self.get_savename(operate + '_ld')
                out_ld.save(save_name, quality=100)

                #切割右上角
                x_ru = int(x + (w - ww))
                y_ru = int(y)
                out_ru = image.crop((x_ru, y_ru, w, hh))
                save_name = self.get_savename(operate + '_ru')
                out_ru.save(save_name, quality=100)

                #切割右下角
                x_rd = int(x + (w - ww))
                y_rd = int(y + (h - hh))
                out_rd = image.crop((x_rd, y_rd, w, hh))
                save_name = self.get_savename(operate + '_rd')
                out_rd.save(save_name, quality=100)

                #切割中心
                x_c = int(x + (w - ww) / 2)
                y_c = int(y + (h - hh) / 2)
                out_c = image.crop((x_c, y_c, ww, hh))
                save_name = self.get_savename(operate + '_c')
                out_c.save(save_name, quality=100)
        
        #日志
        except Exception as e:
            logger.error("ERROR %s", operate)
            logger.error(e)










            









    


