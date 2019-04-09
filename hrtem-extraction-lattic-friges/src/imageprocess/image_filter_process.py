#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_filter_process.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 11:36:15 2019
# Description: ¿¿¿¿¿¿
#************************************************************************#


class imageFilter(object):
    '''
        ¿¿¿¿¿¿
    '''
    def __init__(self):
        pass

    def mean_filter_image(self, im):
        '''
            ¿¿opencv¿¿¿¿¿¿
            ¿¿¿¿:
                result = cv2.blur(¿¿¿¿ ,¿¿¿)
            ¿¿:
                ¿¿¿¿(¿¿, ¿¿)¿¿¿¿¿¿¿,
                ¿¿¿¿¿¿¿(3, 3)¿(5, 5)
        '''
        #img = cv2.imread('test01.png')
        im_source = cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)

        # ¿¿¿¿
        im_result = cv2.blur(im_source, (5, 5))

        # ¿¿¿¿
        titles = ['Source Image', 'Blur Image'] 
        blur_image = [im_source, im_result] 
        for i in range(2): 
            plt.subplot(1,2,i+1)
            plt.imshow(blur_images[i], 'gray') 
            plt.title(titles[i]) 
            plt.xticks([])
            plt.yticks([]) 
        
        plt.show() 
        
        return im_source, im_result, blur_image


    def box_filter_image(self, im):
        '''
            ¿¿opencv¿¿¿¿¿¿
            ¿¿¿¿: 
                result = cv2.boxFilter(¿¿¿¿, ¿¿¿¿¿¿, ¿¿¿, normalize¿¿)
            ¿¿:
                ¿¿¿¿¿¿¿int¿¿, ¿¿¿"-1"¿¿¿¿¿¿¿¿¿;
                ¿¿¿¿¿¿¿(3, 3)¿(5, 5)
        '''
        im_source = cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)
        
        #¿¿¿¿
        im_result = cv2.boxFilter(im_source, -1, (5,5), normalize=1) 
        
        #¿¿¿¿
        titles = ['Source Image', 'BoxFilter Image'] 
        box_filter_image = [im_source, im_result] 
        
        for i in range(2): 
            plt.subplot(1,2,i+1)
            plt.imshow(box_filter_image[i], 'gray') 
            plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([])
    
    plt.show() 
    
    return im_source, im_result, box_filter_image


    def gaussian_blur_filter_image(self, im):
        '''
            ¿¿opencv¿¿¿¿¿¿
            ¿¿¿¿:
                dst = cv2.GaussianBlur(src, ksize, sigmax)
            ¿¿:
                ¿¿¿¿¿¿¿int¿¿, ¿¿¿"-1"¿¿¿¿¿¿¿¿¿
                ¿¿¿¿¿¿¿(3, 3)¿(5, 5)
        '''
        im_source = cv2.cvtColor(self.im,cv2.COLOR_BGR2RGB) 
        
        #¿¿¿¿ 
        im_result = cv2.GaussianBlur(im_source, (3,3), 0) 
        
        #¿¿¿¿
        titles = ['Source Image', 'GaussianBlur Image'] 
        gaussian_filter_image = [im_source, im_result] 
        
        for i in range(2): 
            plt.subplot(1,2,i+1)
            plt.imshow(gaussian_filter_image[i], 'gray') 
            plt.title(titles[i]) 
            plt.xticks([])
            plt.yticks([]) 
        
        plt.show() 
        
        return im_source, im_result, gaussian_filter_image


    def median_blur_filter_image(self, im):
        '''
            ¿¿opencv¿¿¿¿¿¿
            ¿¿¿¿:
                dst = cv2.medianBlur(src, ksize)
            ¿¿:
                src¿¿¿¿¿, ksize¿¿¿¿¿;
                ¿¿¿¿¿¿1¿¿¿, ¿3¿5¿7¿
        '''
        
        #¿¿¿¿
        im_result = cv2.medianBlur(self.im, 3) 
        
        #¿¿¿¿
        cv2.imshow("source img", self.im) 
        cv2.imshow("medianBlur", im_result) 
        
        #¿¿¿¿
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
        
        return self.im, im_result


