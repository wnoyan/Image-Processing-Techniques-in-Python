# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:12:16 2020

@author: Noyan Ali
"""
import cv2
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
img_ref = cv2.imread('lena.jpg', 0)

height = img.shape[0]
width = img.shape[1]
pixels = height * width

height_ref = img_ref.shape[0]
width_ref = img_ref.shape[1]
pixels_ref = height_ref * width_ref

hist = histogram(img)
cum_hist = cumulative_histogram(hist)

hist_ref = histogram(img_ref)
cum_hist_ref = cumulative_histogram(hist_ref)

prob_cum_hist = cum_hist / pixels
prob_cum_hist_ref = cum_hist_ref / pixels_ref

k = 256
new_values = np.zeros((k))

for a in np.arange(k):
    j = k - 1
    while True:
        new_values[a] = j
        j = j - 1
        if j < 0 or prob_cum_hist[a] > prob_cum_hist_ref[j]:
            break

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = new_values[a]
        img_out.itemset((i, j), b)
        
titles = ['Original Image', 'Histogram Matched Image', 'Reference Image']
        
# displaying histograms of original, histogram matched and reference image's respectively
plt.subplot(221), plt.hist(img.ravel(), 256, [0, 256])
plt.title(titles[0])
plt.subplot(222), plt.hist(img_out.ravel(), 256, [0, 256])
plt.title(titles[1])
plt.subplot(223), plt.hist(img_ref.ravel(), 256, [0, 256])
plt.title(titles[2])
plt.show()

cv2.imshow('Input Image', img)
cv2.imshow('Histogram Matched Image', img_out)
cv2.imshow('Referenced Image', img_ref)
cv2.waitKey(0)
cv2.destroyAllWindows()
