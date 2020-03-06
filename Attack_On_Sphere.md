```python
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from spherical_geometry import polygon
from spherical_geometry import vector



    

class disk:
    def __init__(self,b,c,w):
        self.radius=b
        self.centre=c
        self.binormal=w
    def disk_polygon(self):
        s=20
        C=polygon.SingleSphericalPolygon.from_cone(vector.vector_to_lonlat(self.centre[0],self.centre[1],self.centre[2])[0],vector.vector_to_lonlat(self.centre[0],self.centre[1],self.centre[2])[1],self.radius,degrees=False,steps=s)
        return C
    def ret_area(self):
        return self.disk_polygon().area()
    def ret_data(self):
        return self.radius, self.centre, self.binormal
    def ret_frame(self):
        return np.array([self.centre,  np.cross(self.binormal/np.linalg.norm(self.binormal),self.centre),self.binormal/np.linalg.norm(self.binormal)])
    def ret_vel(self):
        return np.cross(self.binormal,self.centre)
    def add_drawing(self,ax,N):
        C=self.disk_polygon().points
        
    
        B= np.array(C).transpose()            
        #print(B)
        ax.plot(B[0],B[1],B[2],c='red',linewidth=1)
        return 0
    def update_attr(self,r,c,w): #Similar to constructor, updates any attributes 
        self.radius=r
        self.centre=c
        self.binormal=w
    def seperate(self,disc):
        r1=self.centre
        r2=disc.centre
        binorm=np.cross(r1,r2)
        binorm=binorm/np.linalg.norm(binorm)
        normal=np.cross(binorm,r1)
        F=[r1,normal,binorm]
        r_1=np.dot(np.linalg.inv(F),r1)
        r_2=np.dot(np.linalg.inv(F),r2)
       
        print(np.linalg.norm(r_2))
        if r_2[0]>1:
            print(r_2)
            r_2[0]=1
           
        elif r_2[0]<-1:
            print(r_2)
            r_2[0]=-1
            
        ang_sep=np.arccos(r_2[0])
        ang1=(ang_sep-self.radius)/2
        ang2=(ang_sep+self.radius)/2
        M1=np.array([[np.cos(ang1),-np.sin(ang1),0],[np.sin(ang1),np.cos(ang1),0],[0,0,1]])
        M2=np.array([[np.cos(ang2),-np.sin(ang2),0],[np.sin(ang2),np.cos(ang2),0],[0,0,1]])
        b1=np.dot(np.dot(F,M1),np.dot(np.linalg.inv(F),self.binormal))
        b2=np.dot(np.dot(F,M2),np.dot(np.linalg.inv(F),disc.binormal))
        
        r_1=np.array([np.cos(ang1),np.sin(ang1),0])
        r_2=np.array([np.cos(ang2),np.sin(ang2),0])
        r1=np.dot(F,r_1)
        r2=np.dot(F,r_2)
        self.update_attr(self.radius,r1,b1)
        disc.update_attr(disc.radius,r2,b2)
        return 0
class Ensemble:#Our mega-class name is Ensemble
    def __init__(self,N,b):#Attributes are N=no. of disks on sphere, b=initial radius of each disk
        self.N=N
        self.b=b
        self.Disk_Arr=[]
        for i in range(N):
            c=np.random.random(3)-np.array([0.5,0.5,0.5]) #Get random position vector to be used as self.centre
            c=c/np.linalg.norm(c) #standard way to normalize vectors.
            n=np.random.random(3)-np.array([0.5,0.5,0.5]) #Get random binormal to be used as self.binormal
            n=n-c*np.dot(n,c)# Ensure binormal is perpendicular by using Gram Schmidt decomposition
            n=n/np.linalg.norm(n) #Normalize binormal
            D=disk(b,c,n) #Create a disk object with initial spherical radius b
            self.Disk_Arr.append(D) #Make a disc list
        self.t=0 #initial time=0
    def draw_ensemble(self,ax):#draws ensemble on Axes3D object ax
        for i in range(self.N):
            self.Disk_Arr[i].add_drawing(ax,5)
    def check_overlap(self):
        for i in range(self.N):
            for j in range(i+1,self.N):
                c1=self.Disk_Arr[i].disk_polygon()
                c2=self.Disk_Arr[j].disk_polygon()
                if c1.intersects_poly(c2):
                    return True
        return False
    def resolve(self):
        s=self.check_overlap
        while(s):
            for i in range(self.N):
                for j in range(i+1,self.N):
                    if self.Disk_Arr[i].disk_polygon().intersects_poly(self.Disk_Arr[j].disk_polygon()):
                        self.Disk_Arr[i].seperate(self.Disk_Arr[j])
                    
                    
            s=self.check_overlap()
        return 0
               
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)          


#Check we can still draw 10 circles as before below:
fig = plt.figure(figsize=plt.figaspect(1.)*2) 
ax = fig.add_subplot(111, projection='3d')

#Turn off the axis planes




#Running in spyder can help you rotate sphere to see result better. Obviously, some overlap.

import time


for i in range(10):
    E=Ensemble(5,0.2)
    ax.cla()
    
    E.resolve()
    E.draw_ensemble(ax)
    print(E.check_overlap())
    time.sleep(5)

    ax.plot_wireframe(x, y, z, color="b",linewidth=0.5) #Get the sphere grid
    ax.set_axis_off()
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    




```
