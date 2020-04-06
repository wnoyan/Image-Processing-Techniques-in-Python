# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:52:36 2020

@author: Noyan Ali
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:14:38 2020

@author: Noyan Ali
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# x and f are image and filter respectively
def convolution(x, f):
    x_height = x.shape[0]
    x_width = x.shape[1]
    
    f_height = f.shape[0]
    f_width = f.shape[1]
    
    h = int((f_height - 1) / 2)
    w = int((f_width - 1) / 2)
    
    out = np.zeros((x_height, x_width))
    
    for i in range(h, x_height-h):
        for j in range(w, x_width-w):
            sum = 0
            for k in range(-h, h+1):
                for l in range(-w, w+1):
                    a = x[i+k, j+l]
                    p = f[h+k, w+l]
                    sum += (a * p)
            out[i, j] = sum
    
    return out

img = cv2.imread('home.jpg', 0)
img_out = img.copy()

height, width = img.shape

# Prewitt Edge in horizontal direction
Hx = np.array([
              [-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]])

# Prewitt Edge in vertical direction
Hy = np.array([
              [-1, -2, -1],
              [0, 0, 0],
              [1, 2, 1]])
    
img_x = convolution(img, Hx) / 8.0
img_y = convolution(img, Hy) / 8.0

img_out = np.sqrt(np.power(img_x, 2) + np.power(img_y, 2))

img_out = (img_out / np.max(img_out)) * 255

plt.imshow(img_out, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()