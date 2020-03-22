import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from spherical_geometry import polygon
from spherical_geometry import vector
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from spherical_geometry import polygon
from spherical_geometry import vector
import time


class disk:
    
    def __init__(self,r,c,w):
        self.r=r #radius
        self.c=c #centre
        self.bi=w
        self.his = [self.c]
       
    def ret_area(self):#Returns area
        return self.ret_cir().area()
    
    def ret_cir(self):#Returns circle as SingleSphericalPolygon
        return polygon.SingleSphericalPolygon.from_cone(vector.vector_to_lonlat(self.c[0],self.c[1],self.c[2])[0]*np.pi/180,vector.vector_to_lonlat(self.c[0],self.c[1],self.c[2])[1]*np.pi/180,self.r,degrees=False)
    
    def ret_data(self):#Returns data
        return self.r, self.c, self.bi
    
    def ret_frame(self):#Returns the Frame Field
        return np.array([self.c,  np.cross(self.bi/np.linalg.norm(self.bi),self.c),self.bi/np.linalg.norm(self.bi)])
    
    def add_drawing(self,ax):#Plots circle on sphere
        C=self.ret_cir().points #points on circle
        B= np.array(C).transpose()            
        h=np.transpose(self.his)
        ax.plot(B[0],B[1],B[2],c='red',linewidth=1)
        #ax.scatter(h[0],h[1],h[2],c='orange') #Uncomment to see the path traced
        return 0
    
    
    def seperate(self,disc):#Seperates two circles if they overlap
       
        r1=self.c
        r2=disc.c
        
        ang=np.arccos(np.dot(r1,r2)) #Find angle between circles
        binorm=np.cross(r1,r2)#Calculate the binormal for the great circle joining circles
        binorm=binorm/np.linalg.norm(binorm)
        normal=np.cross(binorm,r1)
        F=np.array([r1,normal,binorm]) #Create a frame for circle 1
        r_1=np.dot(np.linalg.inv(F),r1) #Bring all circles to xy plane
        r_2=np.dot(np.linalg.inv(F),r2)
        angshift=self.r-ang/2 #Calculate angle by which the centres will be shifted
        R1=np.array([[np.cos(angshift),np.sin(angshift),0],[-np.sin(angshift),np.cos(angshift),0],[0,0,1]])
        R2=np.array([[np.cos(angshift),-np.sin(angshift),0],[np.sin(angshift),np.cos(angshift),0],[0,0,1]])
        r_1=np.dot(R1,r_1) #Rotate centres on XY plane
        r_2=np.dot(R2,r_2)
        r1=np.dot(F,r_1)#Go back from xy plane to great circle
        r2=np.dot(F,r_2)
        v1=np.cross(self.bi,self.c) #Calculate new velocities/tangents for consistency
        v2=np.cross(disc.bi,disc.c)
        self.c=r1 #Update centres
        disc.c=r2
        
    
        self.bi=np.cross(self.c,v1) #Update binormal
        disc.bi=np.cross(disc.c,v2)
        
        
   
        return 0
    
    def parallel(self,disc): #Performs parallel transport. Executed after seperate
        c1=self.c
        c2=disc.c
        binorm=np.cross(c1,c2) #Get great circle binormal
        binorm=binorm/np.linalg.norm(binorm)
        #Parallel transport begins
        vel1=np.cross(binorm,c1)
        v1=np.cross(self.bi,c1)
        t11=np.dot(v1,binorm)
        t12=np.dot(v1,vel1)
        #print(np.dot(vel1,binorm))
        vel2=np.cross(binorm,c2)
        v2=np.cross(disc.bi,c2)
        t21=np.dot(v2,binorm)
        t22=np.dot(v2,vel2)
        #print(np.dot(vel2,binorm))
        c=(c1+c2)/2
        c=c/np.linalg.norm(c)
        v11=t11*binorm+t22*vel1
        v22=t21*binorm+t12*vel2
        #End of parallel transport
        #Update binormals
        self.bi=np.cross(c1,v11)
        disc.bi=np.cross(c2,v22)
        #print(self.bi)
        #print(np.linalg.norm(self.bi))
        #print(disc.bi)
        #print(np.linalg.norm(disc.bi))
        
        
        
        
class Ensemble:#Our mega-class name is Ensemble
    def __init__(self,b):#Attributes are N=no. of disks on sphere, b=initial radius of each disk
        self.N=0
        self.b=b
        self.Disk_Arr=[]
        self.t=0 #initial time=0
        
        
    def draw_ensemble(self,ax):#draws ensemble on Axes3D object ax
        for i in range(self.N):
            self.Disk_Arr[i].add_drawing(ax)
############ DISK_ARR[I] IS A DISK CLASS? #####################################
            
            
    def check_overlap(self): #Checks intersections using spherical-geometry
        for i in range(self.N):
            for j in range(i+1,self.N):
                c1=self.Disk_Arr[i].ret_cir()
                c2=self.Disk_Arr[j].ret_cir()
                if c1.intersects_poly(c2):
                    return True
        return False
    
    
    def resolve(self): #AT each timestep, check overlap
        s=self.check_overlap
        #While there is overlap: seperate and parallel transport disks
        while(s):
            for i in range(self.N):
                for j in range(i+1,self.N):
                    if self.Disk_Arr[i].ret_cir().intersects_poly(self.Disk_Arr[j].ret_cir()):
                        self.Disk_Arr[i].seperate(self.Disk_Arr[j])
                        self.Disk_Arr[i].parallel(self.Disk_Arr[j])
                        
                    
                    
            s=self.check_overlap()
        return 0
    
    
    def add_disk(self,D):#Used to add a circle object on the sphere
        self.Disk_Arr.append(D)
        self.N+=1
        
        
    def move(self):#Move simulation by 1 timestep
        dt=0.01 #Timestep size
        self.t+=dt #Update time
        
        
        for i in range(self.N): #Move disks
            F = self.Disk_Arr[i].ret_frame()
            self.Disk_Arr[i].c=self.Disk_Arr[i].c+(F[1])*np.tan(np.linalg.norm(self.Disk_Arr[i].bi)*dt)
            self.Disk_Arr[i].c=self.Disk_Arr[i].c/np.linalg.norm(self.Disk_Arr[i].c)
            self.Disk_Arr[i].his.append(self.Disk_Arr[i].c)
            #print(self.Disk_Arr[i].c)
            
            Optimal_radius = np.sqrt((4*np.pi)/(self.N*np.pi))
            while self.Disk_Arr[i].r < 0.4*Optimal_radius :
                self.Disk_Arr[i].r += 0.001
            self.Disk_Arr[i].r += (Optimal_radius - self.Disk_Arr[i].r) * 0.001
            print(self.Disk_Arr[i].r)
            
            
            
            
#            self.Disk_Arr[i].r += 0.001 #CONSTANT GROWTH MODEL
        self.resolve() #Resolve any overlaps/collisions
        
            
### JULIANNA'S TRIAL CORNER ########
# 1: Get a gauge for the ultimate radius
# 2: Constant growth until 50% of that radius?
# 3: Once 50% reached, the growth will be (Optimal-current)/100?

#Optimal_radius = np.sqrt((4*np.pi)/(N*np.pi))
#while self.Disk_Arr[i].r < 0.5*Optimal_radius :
#    self.Disk_Arr[i].r += 0.001
#self.Disk_Arr[i].r += (Optimal_radius - self.Disk_Arr[i].r)/1000
        
#Problems faced:
        #Stop condition will never activate?????
        #How to stop???
# 1: When overlap function runs for 2* no. of balls loops consecutively, brute force stop? (need counter)
    
### JULIANNA'S TRIAL CORNER ########
# 1: Get a gauge for the uncovered area
# 2: Constant growth until uncovered area is 50% original area?
# 3: Once 50% reached, the growth will be uncovered area/1000 (exact proportions not tested)?

#Extra_Area = 4*np.pi - N*self.Disk_Arr[i].ret_area()
# while 4*np.pi - self.N*self.Disk_Arr[i].ret_area() > 2*np.pi:
#       self.Disk_Arr[i].r += 0.001
#self.Disk_Arr[i].r += (np.sqrt((4*np.pi - self.N*self.Disk_Arr[i].ret_area()))/self.N)/100
        
    
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
b_0=0.2
M=6
E=Ensemble(b_0) #0.2 is initial radius
for i in range(M): #M is no. of circles
    c=np.random.random(3)-np.array([0.5,0.5,0.5])
    c=c/np.linalg.norm(c)
   
    w=np.random.random(3)-np.array([0.5,0.5,0.5])
    w=w-np.dot(w,c)*c
    w=w*10/np.linalg.norm(w) #Change 10 for different velocities
    C1=disk(b_0,c,w)
    E.add_disk(C1)

while True:
    fig.canvas.draw()
    fig.canvas.flush_events()
    #print('s')
    E.move()
    #for i in range(E.N):
     #   print(np.dot(E.Disk_Arr[i].c,E.Disk_Arr[i].bi))
        
    ax.cla()
    

    E.draw_ensemble(ax)
    #print('s')
    

    ax.scatter(x, y, z, color="y",linewidth=0.5,s=0.1) #Get the sphere grid
    ax.set_axis_off()