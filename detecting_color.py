#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:40:54 2019

@author: computervision
"""

from clusters import Cluster
from back import Back
from selector import Selector
from color_detect import ColorDetector
import matplotlib.pyplot as plt
import numpy as np

im = plt.imread('/home/computervision/Documentos/color_dataset/yellow/101.jpg')
remover = Back(10)
imb = remover.remove_bg(im)
img = im[~imb]

plt.subplot(1,2,1)
plt.imshow(imb)
plt.subplot(1,2,2)
plt.imshow(im)
plt.show()
        
cl = Cluster()
result = cl.clusterize(img)
print("centroides encontradas: ")
print(result)
print('\n')


sl = Selector()
cent = np.array(sl.largest(result[0], result[1], result[2])[0])
print("centroide escolhida: ")
print(cent)
print('\n')


det = ColorDetector()
c = det.color_of(cent)
        
print("Color of vehicle: " + c)