#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:00:57 2019

@author: computervision
"""

from clusters import Cluster
from back import Back
from selector import Selector
from color_detect import ColorDetector
import numpy as np

class Color():
    def __init__(self):
        self.thresh = 10
        self.rm = Back(self.thresh)
        self.cl = Cluster()
        self.sl = Selector()
        self.dt = ColorDetector()
        
    def color(self, img):
        mask = self.rm.remove_bg(img)
        segmented = img[~mask]
        
        centroids = self.cl.clusterize(segmented)
        
        cent = np.array(self.sl.largest(centroids[0], centroids[1], centroids[2])[0])
        
        return self.dt.color_of(cent)
    

