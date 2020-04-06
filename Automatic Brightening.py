# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:16:32 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

brightness = 50

height = img.shape[0]
width = img.shape[1]

for i in np.arange(height):
    for j in  np.arange(width):
        a = img.item(i, j)
        b = a + brightness
        if b > 255:
            b = 255
        img_out.itemset((i, j), b)

cv2.imshow('Input Image', img)
cv2.imshow('Output Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()