# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:23:54 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

# 5x5 Gaussian Filter
gaussian = (1.0 / 57) * np.array(
        [[0,1,2,1,0],
         [1,3,5,3,1],
         [2,5,9,5,2],
         [1,3,5,3,1],
         [0,1,2,1,0]])
#sum(sum(gaussian))

for i in np.arange(2, height-2):
    for j in np.arange(2, width-2):
        sum = 0
        for k in np.arange(-2, 3):
            for l in np.arange(-2, 3):
                a = img.item(i+k, j+l)
                p = gaussian[2+k, 2+l]
                sum = sum + (p * a)
        b = sum
        img_out.itemset((i, j), b)
        
cv2.imshow('Input Image', img)
cv2.imshow('Gaussian Blurred Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()