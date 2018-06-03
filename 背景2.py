# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:15:35 2018

@author: Administrator
"""

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('1.mp4')
fgbg = cv.createBackgroundSubtractorMOG2()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()