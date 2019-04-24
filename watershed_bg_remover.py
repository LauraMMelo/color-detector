#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:45:54 2019

@author: computervision
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import scharr, gaussian
from skimage.color import rgb2gray
from skimage.morphology import watershed

img = plt.imread('./imgs/redcar.jpg')
#plt.imshow(img)
#img = rgb2gray(img)
img = gaussian(img, sigma=2)

edge_scharr = scharr(img[:,:,0]) + scharr(img[:,:,1]) + scharr(img[:,:,2])

#plt.imshow(edge_scharr)





seeds = np.zeros(edge_scharr.shape)
seeds[125, 150] = 1
seeds[0,0] = 2
seeds[-1,0] = 2
seeds[0,-1] = 2
seeds[1,1] = 2

final = watershed(edge_scharr, seeds)
plt.imshow(final)
