# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:54:29 2020

@author: Noyan Ali
"""

import cv2

img = cv2.imread('home.jpg', 0)
img_out = img.copy()

height, width = img.shape

threshold = 127

for i in range(height):
    for j in range(width):
        a = img.item(i, j)
        if a > threshold:
            b = 255
        else:
            b = 0
        img_out.itemset((i, j), b)

cv2.imshow('Input Image', img)
cv2.imshow('Thresholded Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()