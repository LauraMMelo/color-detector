#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:16:35 2019

@author: computervision
"""

from Color import Color
import matplotlib.pyplot as plt
from cv2 import resize
#import pandas as pd
#import numpy as np
import os


detector = Color()
path = '/home/computervision/Documentos/color_dataset/'

results = []
for name in os.listdir(path):
    for item in os.listdir(path + name):
        img = plt.imread(path + name + "/" + item)
        img = resize(img, (300, 300))
        detected_color = detector.color(img)
        true_color = name
        line = [true_color, detected_color, str(path + name + "/" + item)]
        results.append(line)
        
with open('results_resized.txt', 'w') as f:
    for item in results:
        f.write("%s\n" % item)

i = 0
for item in results:
    if item[0] == item[1]:
        i = i + 1

accuracy = i/len(results)
print('Accuracy: ' + str(accuracy))