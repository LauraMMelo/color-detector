from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from back import Back
from mpl_toolkits.mplot3d import Axes3D

im = plt.imread('redcar.jpg')
remover = Back(10)
imb = remover.remove_bg(im)
img = im[~imb]

def _square_distorsion(npixels, compact, y):
        return pow(compact / npixels, -y)
    
def _kmeans(img, k):
        kmeans = KMeans(n_clusters = k, max_iter = 100, tol = 1.0)
        kmeans.fit(img)

        return kmeans.inertia_, kmeans.labels_, kmeans.cluster_centers_

class Cluster():
    def __init__(self):
        self.min_k = 2
        self.max_k = 7
    
    def clusterize(self, img):
        npixels = img.size

        best = None
        prev_distorsion = 0
        largest_diff = float('-inf')

        for k in range(self.min_k, self.max_k):
            compact, labels, centers = _kmeans(img, k)
            distorsion = _square_distorsion(npixels, compact, 1.5)
            diff = prev_distorsion - distorsion
            prev_distorsion = distorsion

            if diff > largest_diff:
                largest_diff = diff
                best = k, labels, centers
        
        return best

    def _square_distorsion(self, npixels, compact, y):
        return pow(compact / npixels, -y)
    
    def _kmeans(self, img, k):
        kmeans = KMeans(n_clusters = k, max_iter = 50, tol = 1.0)
        kmeans.fit(img)

        return kmeans.inertia_, kmeans.labels_, kmeans.cluster_centers_


#plt.plot(img)
        


cl = Cluster()
result = cl.clusterize(img)
print(result)

#plt.imshow(imb)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(img[:,0], img[:,1], img[:,2], color=[(r[0] / 255., r[1] / 255., r[2] / 255.) for r in img], alpha=0.01)
i = result[2]
for j in i:
    ax.scatter(j[2], j[1], j[0], 'x', marker = 'D')
plt.show()