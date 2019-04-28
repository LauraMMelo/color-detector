from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from back import Back
from mpl_toolkits.mplot3d import Axes3D



class Cluster():
    def __init__(self):
        self.min_k = 2
        self.max_k = 7
    
    def _square_distorsion(self, npixels, compact, y):
        return pow(compact / npixels, -y)
    
    def _kmeans(self, img, k):
        kmeans = KMeans(n_clusters = k, max_iter = 50, tol = 1.0)
        kmeans.fit(img)

        return kmeans.inertia_, kmeans.labels_, kmeans.cluster_centers_

    def clusterize(self, img):
        npixels = img.size

        best = None
        prev_distorsion = 0
        largest_diff = float('-inf')

        for k in range(self.min_k, self.max_k):
            compact, labels, centers = self._kmeans(img, k)
            distorsion = self._square_distorsion(npixels, compact, 1.5)
            diff = prev_distorsion - distorsion
            prev_distorsion = distorsion

            if diff > largest_diff:
                largest_diff = diff
                best = k, labels, centers
        
        return best


