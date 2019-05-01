from back import Back
from clusters import Cluster
from selector import Selector
import numpy as np
import matplotlib.pyplot as plt
from cv2 import resize
#from skimage.transform import resize

class Dataset():
    def __init__(self):
        pass

    def to_pixels(self, seg, centr):
        '''
            seg = list of segmented pixels
            centr = output of clusterize()
        '''
        cent = np.array(sl.largest(centr[0], centr[1], centr[2]))
        list_of_pixels = []
        for i in range(len(centr[1])):
            if centr[1][i] == cent[1]:
                list_of_pixels.append(seg[i])
            i = i + 1

        return list_of_pixels



img = plt.imread('./color_examples/blue.jpg')
img = resize(img, (150, 150))
#plt.imshow(img)
#plt.show()


rm = Back(10)
cl = Cluster()
sl = Selector()
dt = Dataset()

mask = rm.remove_bg(img)
segmented = img[~mask]

centroids = cl.clusterize(segmented)

list_of_pix = np.array(dt.to_pixels(segmented, centroids))


print(list_of_pix)
print('\n' + ' Found: ')
print(len(list_of_pix))
print('\n' + ' Total: ')
print(len(segmented))
