# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:58:28 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

max = 0
min = 255

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        if a > max:
            max = a
        if a < min:
            min = a

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = float(a - min) / (max - min) * 255
        img_out.itemset((i, j), b)
        
cv2.imshow('Input Image', img)
cv2.imshow('Contrasted Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()