# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:21:53 2020

@author: Noyan Ali
"""

import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

# return calculated histogram 
def histogram(img):
    height = img.shape[0]
    width = img.shape[1]
    
    hist = np.zeros((256))
    
    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i, j)
            hist[a] += 1
            
    return hist

# return calculated cumulative histogram
def cumulative_histogram(hist):
    cum_hist = hist.copy()
    
    for i in np.arange(1, 256):
        cum_hist[i] = cum_hist[i - 1] + cum_hist[i]
    
    return cum_hist

img = cv2.imread('messi5.jpg', 0)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

pixels = height * width

hist = histogram(img)
cum_hist = cumulative_histogram(hist)

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = math.floor(cum_hist[a]) * 255 / pixels
        img_out.itemset((i, j), b)
        
titles = ['Original Image', 
          'Histogram Equalized Image']

# displaying histograms of original and histogram equalized image's respectively
plt.subplot(221), plt.hist(img.ravel(), 256, [0, 256])
plt.title(titles[0])
plt.subplot(222), plt.hist(img_out.ravel(), 256, [0, 256])
plt.title(titles[1])
plt.show()

cv2.imshow('Input Image', img)
cv2.imshow('Equalized Histogram Image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
