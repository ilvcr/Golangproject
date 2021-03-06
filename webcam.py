# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:32:40 2017

@author: gao->ilvcr

Description：sudo apt-get install python-openCV
"""

__author__ = "yoghourt->gao"


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    #Capture frame-by-frame
    ret, frame = cap.read()
    
    #Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()





