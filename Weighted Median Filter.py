# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:04:14 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

img = cv2.imread('messi5.jpg', 0)
img_out = img.copy()

height, width = img.shape

weights = np.array([[0,0,1,2,1,0,0],
                    [0,1,2,3,2,1,0],
                    [1,2,3,4,3,2,1],
                    [2,3,4,5,4,3,2],
                    [1,2,3,4,3,2,1],
                    [0,1,2,3,2,1,0],
                    [0,0,1,2,1,0,0]])

M = int((sum(sum(weights)) - 1) / 2)

for i in range(3, height-3):
    for j in range(3, width-3):
        neighbors = []
        for k in range(-3, 4):
            for l in range(-3, 4):
                a = img.item(i+k, j+l)
                w = weights[3+k, 3+l]
                for _ in range(w):
                    neighbors.append(a)
        neighbors.sort()
        median = neighbors[M]
        img_out.itemset((i, j), median)

cv2.imshow('Input Image', img)
cv2.imshow('Weighted Median Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()