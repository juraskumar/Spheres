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

https://stackoverflow.com/questions/13901106/plotting-sphere-grid-with-matplotlib-basemap

Code 1: Displays sphere grid
```python
# importing required modules 
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt 
from matplotlib import style 
import numpy as np 
  
# setting a custom style to use 
style.use('ggplot') 
  
# create a new figure for plotting (to add axes & chanf)
#fig = plt.figure() 
fig = plt.figure(figsize=plt.figaspect(1.0)*1.5) 


# create a new subplot on our figure 
ax1 = fig.add_subplot(111, projection='3d') 
  
# get points for a mesh grid 
u, v = np.mgrid[0:2*np.pi:1000j, 0:np.pi:1000j] 
#the higher the values, the greater the mesh
  
# setting x, y, z co-ordinates 
x=np.cos(u)*np.sin(v) 
y=np.sin(u)*np.sin(v) 
z=np.cos(v) 
  
# plotting the curve 
ax1.plot_wireframe(x, y, z, rstride = 5, cstride = 5, linewidth = 1) 
#usual values of rstride and cstride is 1
#the smaller the value of rstride and cstride, the greater the mesh
  
plt.show()
```

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=plt.figaspect(1.0)*1.5) 

ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)


u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)

ax.plot_wireframe(x, y, z, color="r")

ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='b')
ax.plot(x,y,z,"o")

plt.show()
```

Li Ting's Code here:

Marcus' Code here:
_________________________________________________________________________________
```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as ran
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

phipre = np.linspace(0, np.pi, 3)
thetapre = np.linspace(0, 2*np.pi, 2)

phi=(phipre)*(np.random.rand(1,np.size(phipre)))
theta=(thetapre)*(np.random.rand(1,np.size(thetapre)))

x = (np.outer(np.sin(theta), np.cos(phi)))
y = (np.outer(np.sin(theta), np.sin(phi)))
z = (np.outer(np.cos(theta), np.ones_like(phi)))

ax.scatter(x, y, z,s=200, c='r', marker='o')


ax = fig.gca(projection='3d')

u1, v1 = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
x1 = np.cos(u1)*np.sin(v1)
y1 = np.sin(u1)*np.sin(v1)
z1 = np.cos(v1)


ax.plot_surface(x1, y1, z1)

plt.show()
```
_________________________________________________________________________________


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
Code 2: Displays Sphere grid and its stereographic projection:
```
import numpy as np
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



#This code snippet displays a sphere

# draw sphere
fig = plt.figure()

fig = plt.figure(figsize=plt.figaspect(1.0)*1.5) 
ax = fig.gca(projection='3d')

u, v = np.mgrid[0:2*np.pi:2000j, 0:np.pi:1000j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
def stereo(x,y,z):
    c=1/(1.0000000000000001-z)
    return x+c*(x),y+y*c
ax.plot_wireframe(x, y, z, color="b",linewidth=0.5)
plt.show()

figs = plt.figure()

figs = plt.figure(figsize=plt.figaspect(1.0)*1.5) 


a, b=stereo(x,y,z)
c, d=stereo(y,z,x)
e, f=stereo(z,x,y)
plt.scatter(a,b,c='blue',s=0.3)
plt.scatter(c,d,c='blue',s=0.3)
plt.scatter(e,f,c='blue',s=0.3)
plt.show()
```
Geraldine's Code here:

Master Code here:
