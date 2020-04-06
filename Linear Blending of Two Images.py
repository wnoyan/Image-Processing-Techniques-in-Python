# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:57:00 2020

@author: Noyan Ali
"""

import cv2

img1 = cv2.imread('messi5.jpg', 0)
img2 = cv2.imread('lena.jpg', 0)

height, width = img1.shape
img2.resize(height, width)
img_out = img1.copy()

alpha = 0.5

for i in range(height):
    for j in range(width):
        a1 = img1.item(i, j)
        a2 = img2.item(i, j)
        b = alpha * a1 + (1 - alpha) * a2
        img_out.itemset((i, j), b)

cv2.imshow('First Input Image', img1)
cv2.imshow('Second Input Image', img2)
cv2.imshow('Output Blended Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()

