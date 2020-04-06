# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:49:11 2020

@author: Noyan Ali
"""

import cv2
import numpy as np

# return calculated histogram 
def histogram(img):
    hist = np.zeros((256))
    height, width = img.shape
    
    for i in range(height):
        for j in range(width):
            a = img.item(i, j)
            hist[a] += 1
    return hist

# return calculated cumulative histogram
def cumulative_histogram(hist):
    cum_hist = hist.copy()
    
    for i in range(1, 256):
        cum_hist[i] = cum_hist[i] + cum_hist[i - 1]
    return cum_hist

img = cv2.imread('messi5.jpg', 0)
img_out = img.copy()

height, width = img.shape
pixels = height * width

hist = histogram(img)
cum_hist = cumulative_histogram(hist)

# cut off percentage (5%)
p = 0.05

a_low = 0
for i in range(256):
    if cum_hist[i] >= pixels * p:
        a_low = i
        break

a_high = 255
for i in range(255, -1, -1):
    if cum_hist[i] <= pixels * (1 - p):
        a_high = i
        break

for i in range(height):
    for j in range(width):
        a = img.item(i, j)
        b = 0
        if a <= a_low:
            b = 0
        elif a >= a_high:
            b = 255
        else:
            b = float(a - a_low) / (a_high - a_low) * 255
        img_out.itemset((i, j), b)

cv2.imshow('Original Input Image', img)
cv2.imshow('Modified Auto Contrast Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()