# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:45:09 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

img = cv2.imread('messi5.jpg', 0)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

# Laplacian Filter
laplacian = (1.0 / 16) * np.array(
        [[0, 0, -1, 0, 0],
         [0, -1, -2, -1, 0],
         [-1, -2, 16, -2, -1],
         [0, -1, -2, -1, 0],
         [0, 0, -1, 0, 0]])
#sum(sum(laplacian))

for i in np.arange(2, height-2):
    for j in np.arange(2, width-2):
        sum = 0
        for k in np.arange(-2, 3):
            for l in np.arange(-2, 3):
                a = img.item(i+k, j+l)
                w = laplacian[2+k, 2+l]
                sum = sum + (a * w)
        b = sum
        img_out.itemset((i, j), b)

cv2.imshow('Input Image', img)
cv2.imshow('Output Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()