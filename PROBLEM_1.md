```python
#Test code
```

PROBLEM 1: MOVE A POINT ON THE SPHERE + DISPLAY BACKGROUND GRID IN OUTPUT

IDEAS:
- fluff(SURAJ)
-
-
-






Julianna's Code here:

Li Ting's Code here:

Marcus' Code here:

Suraj's Code here:

Code 1: Displays sphere grid
```python
import numpy as np
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



#This code snippet displays a sphere
# Create a sphere
def axisEqual3D(ax):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)



# Create a sphere
# draw sphere
fig = plt.figure()
fig = plt.figure(figsize=plt.figaspect(1.0)*1.5) 
ax = fig.gca(projection='3d')

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

ax.plot_wireframe(x, y, z, color="b",linewidth=0.5)
plt.show()
```

Geraldine's Code here:

Master Code here:
