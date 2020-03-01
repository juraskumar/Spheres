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
Code 1: Displays sphere grid
```python
# importing required modules 
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt 
from matplotlib import style 
import numpy as np 
  
# setting a custom style to use 
style.use('ggplot') 
  
# create a new figure for plotting 
fig = plt.figure() 
  
# create a new subplot on our figure 
ax1 = fig.add_subplot(111, projection='3d') 
  
# get points for a mesh grid 
u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j] 
  
# setting x, y, z co-ordinates 
x=np.cos(u)*np.sin(v) 
y=np.sin(u)*np.sin(v) 
z=np.cos(v) 
  
# plotting the curve 
ax1.plot_wireframe(x, y, z, rstride = 5, cstride = 5, linewidth = 1) 
  
plt.show()
```

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)
ax.plot_wireframe(x, y, z, color="r")

#ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
ax.plot(x,y,z,"o")

plt.show()
```

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
# draw sphere
fig = plt.figure()
fig = plt.figure(figsize=plt.figaspect(1.0)*1.5) 
ax = fig.gca(projection='3d')

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
#Can do projection of (x,y,z)->(a,b)
ax.plot_wireframe(x, y, z, color="b",linewidth=0.5)
plt.show()
```

Geraldine's Code here:

Master Code here:
