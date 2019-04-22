#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:44:59 2019

@author: computervision
"""

import numpy as np
from skimage.io import imread
from skimage.transform import resize
import skimage.filters as skf
import skimage.color as skc
import skimage.morphology as skm
from skimage.measure import label
import matplotlib.pyplot as plt

def _scharr(img):
    img = 1. - img
    grey = skc.rgb2gray(img)
    return skf.scharr(grey)
        


class bg_remover():
    
    def __init__(self, max_distance, use_lab):
        self.max_distance = max_distance
        self.use_lab = use_lab
        
    def corner_mask(self, img):
        h, w = img.shape[:2]
        mask = np.zeros((h, w), dtype=np.bool)
        max_distance = 5
        
        if self.use_lab == True:
            img = skc.rgb2lab(img)
        
        corners = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
        for color in (img[i, j] for i, j in corners):
            norm = np.sqrt(np.sum(np.square(img - color), 2))
            mask |= norm < max_distance
            
        return mask
    
    def floodfill(self, img):
        back = _scharr(img)
        back = back > 0.05

        back = skm.skeletonize(back)

        back[0, :] = back[-1, :] = True
        back[:, 0] = back[:, -1] = True

        labels = label(back, background=-1, connectivity=1)

        corners = [(1, 1), (-2, 1), (1, -2), (-2, -2)]

        for l in (labels[i, j] for i, j in corners):
            back[labels == l] = True

        return skm.opening(back)
        
    def full_mask(self, img):
        f = self.floodfill(img)
        g = self.corner_mask(img)
        m = f | g

        if np.count_nonzero(m) < 0.90 * m.size:
            return m

        ng = np.count_nonzero(g)
        nf = np.count_nonzero(f)

        if ng < 0.90 * g.size and nf < 0.90 * f.size:
            return g if ng > nf else f

        if ng < 0.90 * g.size:
            return g

        if nf < 0.90 * f.size:
            return f

        return np.zeros_like(m)
