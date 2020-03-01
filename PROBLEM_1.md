```python
#Test code
```

PROBLEM 1: MOVE A POINT ON THE SPHERE + DISPLAY BACKGROUND GRID IN OUTPUT

IDEAS:
- Refer to jupyter file named Frame Fields in the main page. Basis for code 3.
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
Code 3: Displays a sphere and draws the path of a random point with a random velocity
```
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

    

phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

def gen_normal_vel(r):
    n=np.random.random(3)
    n=n-np.dot(n,r)*r
    m=np.linalg.norm(n)
    n=n/m
    b=np.cross(r,n)
    return np.array([r,n,b])
def gen_path_from_frame(F,w,ang,dt):
    ang=ang+w*dt
    vec=np.array([np.cos(ang),np.sin(ang),0])
    vec=np.dot(F,vec)
    return vec,ang

    

# The Cartesian coordinates of the unit sphere
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)
col=0.45#Change to change color.
fcolors = np.meshgrid(np.ones(100)*col,np.zeros(100))[0]
w=1
N=8000
ang=0
dt=0.01

r=np.random.random(3)
r=r/np.linalg.norm(r)
F=gen_normal_vel(r)
X=[r[0]*1.01]
Y=[r[1]*1.01]
Z=[r[2]*1.01]

for i in range(N):
    r,ang=gen_path_from_frame(F,w,ang,dt)
    X.append(r[0]*1.01)
    Y.append(r[1]*1.01)
    Z.append(r[2]*1.01)
  
    
    


# Set the aspect ratio to 1 so our sphere looks spherical
fig = plt.figure(figsize=plt.figaspect(1.)*2)
ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x, y, z,  rstride=10, cstride=10, facecolors=cm.seismic(fcolors))
ax.plot(X[1:],Y[1:],Z[1:],'ro',linewidth=0.1)
ax.plot_wireframe(x, y, z, color="b",linewidth=0.5)
#Turn off the axis planes
ax.set_axis_off()



plt.show()

```
Geraldine's Code here:

Master Code here:
