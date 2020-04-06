# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:26:03 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

# 7x7 box is used
for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):
        sum = 0
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                sum = sum + a
        b = int(sum / 49.0)
        img_out.itemset((i, j), b)

cv2.imshow('Input Image', img)
cv2.imshow('Blurred Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()