
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

class Back():
    def __init__(self, max_distance):
        self.max_distance = max_distance
        
    
    def remove_bg(self, img):

        h, w = img.shape[:2]
        mask = np.zeros((h, w), dtype=np.bool)

        img = skf.gaussian(img, sigma=1)
        img = skc.rgb2lab(img)

        corners = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
        for color in (img[i, j] for i, j in corners):
            norm = np.sqrt(np.sum(np.square(img - color), 2))
            mask |= norm < self.max_distance

        back = _scharr(img)
        back = back > 0.05

        back = skm.skeletonize(back)

        back[0, :] = back[-1, :] = True
        back[:, 0] = back[:, -1] = True

        labels = label(back, background=-1, connectivity=1)

        corners = [(1, 1), (-2, 1), (1, -2), (-2, -2)]

        for l in (labels[i, j] for i, j in corners):
            back[labels == l] = True

        result = skm.opening(back)

        f = mask
        g = result
        m = f | g
        
        return m

