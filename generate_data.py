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
                list_of_pixels.append(tuple(seg[i].tolist()))
            i = i + 1

        return list_of_pixels
    
    def CountFrequency(self, my_list):
        freq = {}
        for item in my_list:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
                
        freq_descending_list = sorted(freq, key=freq.get, reverse=True)
        
        freq_descending = {}
        for item in freq_descending_list:
            freq_descending[item] = freq[item]
            
        return freq_descending



        

     

img = plt.imread('./color_examples/red.jpg')
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

list_of_pix = dt.to_pixels(segmented, centroids)

freq_pixels = dt.CountFrequency(list_of_pix)


print(list_of_pix)
print('\n' + ' Found: ')
print(len(list_of_pix))
print('\n' + ' Total: ')
print(len(segmented))
print('\n' + 'Most frequent: ')
for x in list(freq_pixels)[0:50]:
    print(x, freq_pixels[x])



