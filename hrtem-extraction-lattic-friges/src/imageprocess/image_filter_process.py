#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_filter_process.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 11:36:15 2019
# Description: 
#************************************************************************#

def mean_filter_image(im):
    '''
        ����OpenCVʵ�־�ֵ�˲�
        ����ԭ��:result = cv2.blur(ԭʼͼ��,�˴�С)
        ����:
            �˴�С���ԣ���ȣ��߶ȣ���ʾ��Ԫ����ʽ;
            ��������ʽ����:�˴�С��3, 3���ͣ�5, 5��
    '''
    #img = cv2.imread('test01.png')
    source = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    # ��ֵ�˲�
    result = cv2.blur(source, (5, 5))

    # ��ʾͼ��
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
        ����OpenCVʵ�ַ����˲�
        ����ԭ��:result = cv2.boxFilter(ԭʼͼ��, Ŀ��ͼ�����, �˴�С, normalize����)
        ����:
            Ŀ��ͼ�������int����;ͨ���á�-1����ʾ��ԭʼͼ��һֱ;
            �˴�С��Ҫ������3;3���ͣ�5;5��
    '''
    source = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    
    #�����˲� 
    result = cv2.boxFilter(source, -1, (5,5), normalize=1) 
    
    #��ʾͼ�� 
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
        ����OpenCVʵ�ָ�˹�˲�
        ����ԭ�ͣ�dst = cv2.GaussianBlur(src, ksize, sigmaX)
        ����,
            Ŀ��ͼ�������int����, ͨ���á�-1����ʾ��ԭʼͼ��һֱ;
            �˴�С��Ҫ������3, 3���ͣ�5, 5��
    '''
    source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    
    #��˹�˲� 
    result = cv2.GaussianBlur(source, (3,3), 0) 
    
    #��ʾͼ�� 
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
        ����OpenCVʵ����ֵ�˲�
        ����ԭ�ͣ�dst = cv2.medianBlur(src, ksize)
        ����:
            src��ʾԴ�ļ�,ksize��ʾ�˴�С;
            �˱����Ǵ���1������, ��3��5��7��
    '''
    #��ȡͼƬ 
    #img = cv2.imread('test01.png') 
    
    #��ֵ�˲� 
    result = cv2.medianBlur(img, 3) 
    
    #��ʾͼ�� 
    cv2.imshow("source img", img) 
    cv2.imshow("medianBlur", result) 
    
    #�ȴ���ʾ 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    
    return result
