# Color Detection via Euclidean Distance

[![N|Solid] (detection.png)]

This is a python script that detects the predominant color of an object in an image. In this specific aplication, we are detecting color of vehicles.



## Pipeline
```mermaid
graph LR

A[Input image] .-> C((Mask))
A -- Remove BG --> B[mask]
B --> C{Color Pixels}
C -- KMeans + Distortion --> D[Centroids]

E[Centroids] -- Largest --> F[Predominant pixels]
F -- Smallest L2 Norm to RGB Values of colors --> G{detection}


```


## Files



## Results




