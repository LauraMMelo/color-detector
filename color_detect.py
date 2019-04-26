#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:41:28 2019

@author: computervision
"""


import scipy 
import math

class ColorDetector():
    def __init__(self):
        self.color_coord = {
                'yellow': [242, 204, 17],
                'white': [255, 255, 255],
                'silver': [187, 197, 206],
                'red': [194, 24, 35],
                'orange': [193, 113, 44],
                'green': [43, 102, 70],
                'gray': [80, 80, 80],
                'crimson': [76, 16, 18],
                'blue': [2, 57, 157],
                'black': [0, 0, 0]
                }
        
    def color_of(self, cent):
        current_dist = math.inf
        for key, value in self.color_coord.items():
            dist = scipy.spatial.distance.euclidean(value, cent)
#            print("Euclidean distance to " + key + ": " + str(dist))
            if dist < current_dist:
                current_dist = dist
                color_name = key
                
        return color_name 
    
    
