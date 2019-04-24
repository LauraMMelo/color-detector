#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:07:23 2019

@author: computervision
"""

import numpy as np

import matplotlib.pyplot as plt
from back import Back
from clusters import Cluster

class Selector():
    def __init__(self):
        self.ratio_thresh = 0.75
        
    def largest(self, k, labels, centers):
        counts = [np.count_nonzero(labels == l) for l in range(k)]
        sort_idx = np.argsort(counts)[::-1]
        return [centers[sort_idx[0]]]
    
    def ratio(self, k, labels, centers):
        counts = [np.count_nonzero(labels == l) for l in range(k)]
        counts = np.array(counts, np.uint32)
        total = np.sum(counts)
        sort_idx = np.argsort(counts)[::-1]
        cum_counts = np.cumsum(counts[sort_idx])
        
        threshold = self.ratio_thresh
        for idx_stop in range(k):
            if cum_counts[idx_stop] >= threshold * total:
                break
        sort_centers = centers[sort_idx]
        return sort_centers[:idx_stop + 1]


#im = plt.imread('./imgs/redcar.jpg')
#remover = Back(10)
#imb = remover.remove_bg(im)
#img = im[~imb]
#
#cl = Cluster()
#result = cl.clusterize(img)
#print(result)
#
#plt.imshow(im)
#
#plt.imshow(imb)
#
#sel = Selector()
#cents = sel.largest(result[0], result[1], result[2])