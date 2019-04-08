# -*- coding: utf-8 -*-
"""
Created on Mon Apr 08 19:28:15 2019

@author: gao->ilvcr

Description： 傅立叶变换->滤波器过滤->反傅立叶变换->
              锐化->反转->均衡化->二值化->提取骨架
"""

__author__ = "yoghourt->gao"



import numpy as np
from PIL import Image
import matplotlib.image as mpimg   # mpimg 用于读取图片
import matplotlib.pyplot as plt    #plt 用于显示图片
from scipy import misc
import cv
import cv2

class image_Handle(object):
    '''
        
    '''
    def __init__(self, image_path, array):
        '''
            图像存储路径
            读取图像
        '''
        self.image_path = r'sample.png'
        self.im = Image.open(image)



def show_image():
    '''
        显示图片
    '''    
    im = Image.open('sample.png')
    im.show()
    
    return im

def save_image_using_Image(im):
    '''
        调用 Image 类的 save 方法保存 PIL 图片
    '''
    #im = Image.open('sample.png')
    im = im.save()
    
    return im
    
def save_image_using_plt(im):
    '''
        保存 matplotlib 画出的图像. 
        适用于保存任何 matplotlib 画出的图像，相当于一个 screencapture
    '''
    plt.imshow(im)
    plt.axis('off')
    
    plt.savefig('new_sample_size.png')

def save_image_using_array(im):
    '''
        将 array 保存为图像
    '''
    misc.imsave('new_sample_size.png', im)

def direct_save_image_using_array(im):
    '''
        直接保存 array, 这种方法完全不会对图像质量造成损失
    '''
    np.save('new_sample_size.png', im) # 会在保存的名字后面自动加上.npy
    img = np.load('new_sample_size.npy') # 读取前面保存的数组
    
    plt.imshow(img) # 显示图片
    plt.axis('off') # 不显示坐标轴
    plt.show()
    
    return img
    
def pil_image2numpy_array(im):
    '''
        将 PIL Image 图片转换为 numpy 数组, 便于处理
    '''
    im_array = np.array(im)

    return im_array    
    
def show_image_using_mping():
    '''
        使用mping显示图片
    '''
    im = mpimg.imread('sample.png') # 这里读入的数据是 float32 型的，范围是0-1
    # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
    im.shape(512, 512, 3)
    
    plt.imshow(im) # 显示图片
    plt.axis('off') # 不显示坐标轴
    plt.show()

def show_onething_channel(im):
    '''
        显示图片的第一个通道
    '''
    im_1 = im[:, :, 0]
    plt.imshow('im_1')
    plt.show()
    '''
        # 此时会发现显示的是热量图，不是我们预想的灰度图，可以添加 cmap 参数，有如下几种添加方法：
        plt.imshow('lena_1', cmap='Greys_r')
        plt.show()

        img = plt.imshow('lena_1')
        img.set_cmap('gray') # 'hot' 是热量图
        plt.show()
    '''
    return im_1
    
def numpy_array2pil_image(im):
    '''
        将 numpy 数组转换为 PIL 图片
    '''
    im = mpimg.imread('lena.png') # 这里读入的数据是 float32 型的，范围是0-1
    im = Image.fromarray(np.uinit8(im*255))
    
    im.show()

def RGB2gray_image(im):
    '''
        RGB 转换为灰度图
    '''
    im = Image.open('sample.png')
    im.show()
    
    im_gray = im.convert('gray')
    im_gray.show()
    
def using_scipy_zoom_image(im):
    '''
        用scipy对图像进行放缩
    '''
    im_new_size = misc.imresize(im, 0.5) 
    # 第二个参数如果是整数，则为百分比，如果是tuple，则为输出图像的尺寸

    plt.imshow(im_new_size)
    
    plt.axis('off')
    plt.show()
    
    
def skeleton_extraction():
    '''
    Skeleton extraction
    骨架提取
    '''
    

def img_fft_using_formula(im):
    '''
        使用公式的图像的傅里叶变换
    '''
    
    # 根据公式转成灰度图
    im = 0.2126 * im[:,:,0] + 0.7152 * im[:,:,1] + 0.0722 * im[:,:,2]
    
    # 显示原图
    plt.subplot(231)
    plt.imshow(im,'gray')
    plt.title('original')
    
    # 进行傅立叶变换，并显示结果
    fft2 = np.fft.fft2(im)
    plt.subplot(232)
    plt.imshow(np.abs(fft2),'gray')
    plt.title('fft2')
    
    # 将图像变换的原点移动到频域矩形的中心，并显示效果
    shift2center = np.fft.fftshift(fft2)
    plt.subplot(233)
    plt.imshow(np.abs(shift2center),'gray')
    plt.title('shift2center')
    
    # 对傅立叶变换的结果进行对数变换，并显示效果
    log_fft2 = np.log(1 + np.abs(fft2))
    plt.subplot(235)
    plt.imshow(log_fft2,'gray')
    plt.title('log_fft2')
    
    # 对中心化后的结果进行对数变换，并显示结果
    log_shift2center = np.log(1 + np.abs(shift2center))
    plt.subplot(236)
    plt.imshow(log_shift2center,'gray')
    plt.title('log_shift2center')
    

def  img_fft_using_cv2(im):
    '''
        使用cv2库的图像的傅里叶变换
    '''
    img = cv2.imread('sample.png',0) 
    
    dft = cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT) 
    plt.subplot(221) 
    plt.axis('off') 
    plt.title('dft') 
    plt.imshow(20*np.log(cv2.magnitude(dft[:,:,0],dft[:,:,1])),cmap='gray') 
    
    dft_shift = np.fft.fftshift(dft) 
    plt.subplot(222) 
    plt.axis('off') 
    plt.title('dft_shift') 
    plt.imshow(20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])),cmap='gray') 
    
    return dft
    
def  img_ifft_using_cv2(im):
    '''
        使用cv2库的图像的反傅里叶变换
    '''
    idft_shift = np.fft.ifftshift(dft_shift) 
    plt.subplot(223) 
    plt.axis('off') 
    plt.title('origin') 
    plt.imshow(img,cmap='gray') 
    
    idft = cv2.idft(idft_shift) 
    plt.subplot(224) 
    plt.axis('off') 
    plt.title('idft_shift') 
    plt.imshow(cv2.magnitude(idft[:,:,0],idft[:,:,1]),cmap='gray') 
    
    plt.show()
    
    return idft

def add_noise_in_image():
    '''
        为图像增加噪声
    '''
    
    # 读取噪声
    im = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
    rows, cols, chn = im.shape
    
    # 增加噪声
    for i in range(5000):    
        x = np.random.randint(0, rows) 
        y = np.random.randint(0, cols)    
        im[x,y,:] = 255
    
    cv2.imshow("noise", im)
    
    # 等待显示
    cv2.waitKey(0)
    cv2.destoryAllWindows()
    
    return im
    
def mean_filter_image(im):
    '''
        调用OpenCV实现均值滤波
        函数原型:result = cv2.blur(原始图像,核大小)
        其中:
            核大小是以（宽度，高度）表示的元祖形式;
            常见的形式包括:核大小（3, 3）和（5, 5）
    '''
    #img = cv2.imread('test01.png')
    source = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    # 均值滤波
    result = cv2.blur(source, (5, 5))

    # 显示图形
    titles = ['Source Image', 'Blur Image'] 
    image = [source, result] 
    for i in xrange(2): 
        plt.subplot(1,2,i+1)
        plt.imshow(images[i], 'gray') 
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([]) 
    
    plt.show() 
    
    return image
  
def box_filter_image(im):
    '''
        调用OpenCV实现方框滤波
        函数原型:result = cv2.boxFilter(原始图像, 目标图像深度, 核大小, normalize属性)
        其中:
            目标图像深度是int类型;通常用“-1”表示与原始图像一直;
            核大小主要包括（3;3）和（5;5）
    '''
    source = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    
    #方框滤波 
    result = cv2.boxFilter(source, -1, (5,5), normalize=1) 
    
    #显示图形 
    titles = ['Source Image', 'BoxFilter Image'] 
    image = [source, result] 
    
    for i in xrange(2): 
        plt.subplot(1,2,i+1)
        plt.imshow(images[i], 'gray') 
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([])
    
    plt.show() 
    
    return image
    
def gaussian_blur_filter_image(im):
    '''
        调用OpenCV实现高斯滤波
        函数原型：dst = cv2.GaussianBlur(src, ksize, sigmaX)
        其中,
            目标图像深度是int类型, 通常用“-1”表示与原始图像一直;
            核大小主要包括（3, 3）和（5, 5）
    '''
    source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    
    #高斯滤波 
    result = cv2.GaussianBlur(source, (3,3), 0) 
    
    #显示图形 
    titles = ['Source Image', 'GaussianBlur Image'] 
    image = [source, result] 
    
    for i in xrange(2): 
        plt.subplot(1,2,i+1)
        plt.imshow(images[i], 'gray') 
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([]) 
    
    plt.show() 
    
    return image
    
def median_blur_filter_image(im):
    '''
        调用OpenCV实现中值滤波
        函数原型：dst = cv2.medianBlur(src, ksize)
        其中:
            src表示源文件,ksize表示核大小;
            核必须是大于1的奇数, 如3、5、7等
    '''
    #读取图片 
    #img = cv2.imread('test01.png') 
    
    #中值滤波 
    result = cv2.medianBlur(img, 3) 
    
    #显示图像 
    cv2.imshow("source img", img) 
    cv2.imshow("medianBlur", result) 
    
    #等待显示 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    
    return result
    
def sharppen_image(im):
    '''
        图像锐化
    '''
    #加载图像
    #image = cv2.imread('../data/lena.jpg')

    #自定义卷积核
    kernel_sharpen_1 = np.array([
            [-1,-1,-1],
            [-1,9,-1],
            [-1,-1,-1]])
    kernel_sharpen_2 = np.array([
            [1,1,1],
            [1,-7,1],
            [1,1,1]])
    kernel_sharpen_3 = np.array([
            [-1,-1,-1,-1,-1],
            [-1,2,2,2,-1],
            [-1,2,8,2,-1],
            [-1,2,2,2,-1], 
            [-1,-1,-1,-1,-1]])/8.0
    #卷积
    im_1 = cv2.filter2D(im,-1,kernel_sharpen_1)
    im_2 = cv2.filter2D(im,-1,kernel_sharpen_2)
    im_3 = cv2.filter2D(im,-1,kernel_sharpen_3)
    
    #显示锐化效果
    cv2.imshow('Original Image', im)
    cv2.imshow('sharpen_1 Image', im_1)
    cv2.imshow('sharpen_2 Image', im_2)
    cv2.imshow('sharpen_3 Image', im_3)
    
    #停顿
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()
    
    return im, im_1, im_2, im_3
    

def image2gray_handle(im):
    '''
        读入正常图像并进行灰度化处理
    '''
    
    #灰度化处理
    gray_im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    return gray_im

def image2two_valued_handle(im):
    '''
        对灰度图像进行二值化处理
    '''
    
    #二值化处理
    ret,im_fixed=cv2.threshold(im,50,255,cv2.THRESH_BINARY)

    return ret, im_fixed
    
def gray_image2gamma_handle(im):
    '''
        对灰度图像进行伽马变换
    '''
    
    #伽马变换
    im_gamma=copy.deepcopy(im)

    rows=im.shape[0]
    cols=im.shape[1]
    for i in range(rows):
        for j in range(cols):
            im_gamma[i][j]=3*pow(im_gamma[i][j],0.8)
    
    return im_gamma
    
def gray_image2log_handle(im):
    '''
        对灰度图像进行对数变换
    '''
    
    # 对数变换
    im_logc = copy.deepcopy(im)
    
    for i in range(rows):
        for j in range(cols):
            im_logc[i][j] = 3 * math.log(1 + im_logc[i][j])
    
    return im_logc
    
def gray_image2cover_color_handle(im):
    '''
        对灰度图像进行反色变换
    '''
    #补色变换
    im_cover=copy.deepcopy(im)
    
    for i in range(rows):
        for j in range(cols):
            im_cover[i][j]=255-im_cover[i][j]
    
    return im_cover
    

from skimage import data,exposure
import matplotlib.pyplot as plt

def image_equalization_handle(im):
    '''
        均衡化处理
    '''
    
    #img=data.moon()
    plt.figure("hist",figsize=(8,8))

    im_arr=im.flatten()
    
    plt.subplot(221)
    plt.imshow(im, plt.cm.gray)  #原始图像
    
    plt.subplot(222)
    plt.hist(im_arr, bins=256, normed=1,edgecolor='None',facecolor='red') #原始图像直方图

    im1=exposure.equalize_hist(im)
    im_arr1=im1.flatten()
    
    plt.subplot(223)
    plt.imshow(im1, plt.cm.gray)  #均衡化图像
    
    plt.subplot(224)
    plt.hist(im_arr1, bins=256, normed=1, edgecolor='None', facecolor='red') #均衡化直方图

    plt.show()
    
    return iml
    

    
    
    
    
    
    
    
    