from back import Back
from clusters import Cluster
from selector import Selector
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize



img = plt.imread('./color_examples/blue.jpg')
img = resize(img, (150, 150))


rm = Back(10)
cl = Cluster()
sl = Selector()

mask = rm.remove_bg(img)
segmented = img[~mask]

centroids = cl.clusterize(segmented)
cent = np.array(sl.largest(centroids[0], centroids[1], centroids[2]))

list_of_indexes = []
for i in range(len(centroids[1])):
    if centroids[1][i] == cent[1]:
        list_of_indexes.append(i)
    i = i + 1

print(list_of_indexes)
print('\n' + ' Found: ')
print(len(list_of_indexes))
print('\n' + ' Total: ')
print(len(segmented))
