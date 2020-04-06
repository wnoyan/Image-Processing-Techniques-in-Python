# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:29:38 2020

@author: Noyan Ali
"""

import cv2

img = cv2.imread('messi5.jpg', 0)
img_out = img.copy()

height, width = img.shape

for i in range(3, height-3):
    for j in range(3, width-3):
        neighbors = []
        for k in range(-3, 4):
            for l in range(-3, 4):
                a = img.item(i+k, j+l)
                neighbors.append(a)
        neighbors.sort()
        # finding median of the neighbors
        median = neighbors[24]
        img_out.itemset((i, j), median)

cv2.imshow('Original Input Image', img)
cv2.imshow('Median Filterred Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()