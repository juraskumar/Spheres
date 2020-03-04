```python
import math
import numpy as np
import matplotlib.pyplot as mp
import time
def rearrange(N,X,Y,L,b):#A function to rearrange starting place.
    s=1
    for i in range(N):
        if s==0:
            break
        for j in range(i+1,N):
    
            x1=X[i]# These are positions of the N molecules
            y1=Y[i]
            x2=X[j]
            y2=Y[j]
            cx=1
            cy=1
            dx=np.abs(x2-x1)
            dy=np.abs(y2-y1)
            if dx**2+dy**2<4*b*b:#If there is overlap
                dd=(dx**2+dy**2)**0.5
                mag=(2*b-dd)#The amount to move
                if x2<x1:
                    cx=-1
                if y2<y1:
                    cy=-1
                X[i]=(x1-cx*dx*mag/dd)%10
       
                Y[i]=(y1-cy*dy*mag/dd)%10
                X[j]=(x2+cx*dx*mag/dd)%10
                Y[j]=(y2+cy*dy*mag/dd)%10
                s=0
                break
    
    return s

def update_col_vel(b,x1,y1,x2,y2,vx1,vy1,vx2,vy2):
    
    v1=np.array([vx1,vy1])
    v2=np.array([vx2,vy2])
    mag=np.sqrt((x2-x1)**2+(y2-y1)**2)
    r=np.array([(x2-x1)/mag,(y2-y1)/mag])
    v11=v1-2*np.dot(v1,r)*r
    v22=v2-2*np.dot(v2,r)*r
    return (v11[0],v11[1],v22[0],v22[1])

def update_wall_vel(vx,vy,w):
    if w==1:
        return(-vx,vy)
    else:
        return (vx,-vy)

def update_col_time(X,Y,Vx,Vy,N,b,L,t):
    tplus=0
    mini=math.inf
    c1=-1
    c2=-1
    ch=0
    w=-1
    for i in range(N):
        if N==1:
            break
        for j in range(i+1,N):
            v_rel=np.array([Vx[j]-Vx[i],Vy[j]-Vy[i]])
            r_rel=np.array([X[j]-X[i],Y[j]-Y[i]])
            #if np.arccos(-np.dot(v_rel/np.linalg.norm(v_rel),r_rel/np.linalg.norm(r_rel)))>=np.arcsin(2*b/np.linalg.norm(r_rel)):
            #    continue
            
            tau=(1/np.linalg.norm(v_rel)**2)*(-np.dot(v_rel,r_rel)-np.sqrt(np.dot(v_rel,r_rel)**2-(np.linalg.norm(v_rel)**2)*(np.linalg.norm(r_rel**2)-4*b*b)))
            if tau<mini and tau>0:
                mini=tau
                c1=i
                c2=j
    tplus=mini            
    k=-1
    for i in range(N):
        tx=math.inf
        ty=math.inf
        if Vx[i]>0:
            tx=(L-X[i]-b)/Vx[i]
        if Vx[i]<0:
            tx=-(X[i]-b)/Vx[i]
        if Vy[i]>0:
            ty=(L-Y[i]-b)/Vy[i]
        if Vy[i]<0:
            ty=-(Y[i]-b)/Vy[i]
        tplus=min([ty,tx,tplus])
        if tplus==tx or tplus==ty:
            k=i
            if tx>ty:
                w=0
            else:
                w=1
    if tplus==mini:
        ch=1
    t=t+tplus
    b=growth(b,tplus,Vx,Vy)
    s=0
    while(s==0):
        s=rearrange(N,X,Y,L,b)
    if ch==1:
        for i in range(len(X)):
            X[i]=(X[i]+Vx[i]*tplus)
            Y[i]=(Y[i]+Vy[i]*tplus)
        (Vx[c1],Vy[c1],Vx[c2],Vy[c2])=update_col_vel(b,X[c1],Y[c1],X[c2],Y[c2],Vx[c1],Vy[c1],Vx[c2],Vy[c2])
    #print('Particles',c1,c2,'colliding at',t)
    else:
        for i in range(len(X)):
            X[i]=(X[i]+Vx[i]*tplus)
            Y[i]=(Y[i]+Vy[i]*tplus)
        Vx[k],Vy[k]=update_wall_vel(Vx[k],Vy[k],w)
    return (X,Y,Vx,Vy,t,b)
    
        
            
def growth(b,tplus,Vx,Vy):
        #return b+tplus*0.9*min(min(Vx),min(Vy))
        return b+tplus*0.01
    
        
t=0    
L=1
N=20
M=100
b=0.02
X=np.random.rand(N)*(L-4*b)+2*b
Y=np.random.rand(N)*(L-4*b)+2*b
Vx=np.random.rand(N)*0.1
Vy=np.random.rand(N)*0.1
s=0
while(s==0):
    s=rearrange(N,X,Y,L,b)
fig = mp.figure()
mp.ylim(0, 1) 
mp.xlim(0, 1) 
ax = fig.add_subplot(111)
 # Returns a tuple of line objects, thus the comma
for i in range(M):
    #tem=t
    ax.cla()
    time.sleep(0.5)
    (X,Y,Vx,Vy,t,b)=update_col_time(X,Y,Vx,Vy,N,b,L,t)
    #mp.scatter(np.asarray(X),np.asarray(Y),s=1000*b)

    #mp.show()
    #print(X,Vx,t,i)
    
    

    #for phase in np.linspace(0, 10*np.pi, 500):
    for i in range(len(X)):
        x=X[i]
        y=Y[i]
        circle1 = mp.Circle((x, y),b , color='r')
        ax.add_artist(circle1)
    fig.canvas.draw()
    fig.canvas.flush_events()
    ```
