#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:16:56 2019

@author: computervision
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from back import Back
from clusters import Cluster
from mpl_toolkits.mplot3d import Axes3D

im = plt.imread('./imgs/corolla.jpg')
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
print(result)



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(img[:,0], img[:,1], img[:,2], color=[(r[0] / 255., r[1] / 255., r[2] / 255.) for r in img], alpha=0.01)
i = result[2]
for j in i:
    ax.scatter(j[2], j[1], j[0], 'x', marker = 'D')
plt.show()

