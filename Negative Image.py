# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:32:38 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

img = cv2.imread('messi5.jpg', 0)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

max_intensity = 255

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = max_intensity - a
        img_out.itemset((i, j), b)

cv2.imshow('Original Image', img)
cv2.imshow('Negative Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()