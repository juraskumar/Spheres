Enter your codes here:

Suraj's Code:

```python

#ALL IMPORTS HERE
import math
import numpy as np
import matplotlib.pyplot as mp
import time
from contextlib import contextmanager
import threading
import _thread

#DEFINE CLASS TO INTRODUCE TIMEOUTS
class TimeoutException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

@contextmanager
def time_limit(seconds, msg=''):
    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        raise TimeoutException("Timed out for operation {}".format(msg))
    finally:
        # if the action ends in specified time, timer is canceled
        timer.cancel()
#TO ENSURE A FUNCTION TIMEOUTS WITHIN T SECONDS USE THIS FORMAT:
'''
with time_limit(<insert T in seconds here as float value>,'<insert func_name>'):
    func_name(func_args)
'''





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
            if dx**2+dy**2<4*b*b-0.005:#If there is overlap, 0.005 is distance parameter
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
        for i in range(N):
            if s==0:
                break
            x=X[i]
            y=Y[i]
            if x>L-b:
                X[i]-=x-L+b
                s=0
            if x<b:
                X[i]+=b-x
                s=0
            if y>L-b:
                Y[i]-=y-L+b
                s=0
            if y<b:
                Y[i]+=b-y
                s=0
        return s

def update_col_vel(b,x1,y1,x2,y2,vx1,vy1,vx2,vy2):#Updates velocities for ball-ball collision
    
    v1=np.array([vx1,vy1])
    v2=np.array([vx2,vy2])
    mag=np.sqrt((x2-x1)**2+(y2-y1)**2)
    r=np.array([(x2-x1)/mag,(y2-y1)/mag])
    v11=v1-2*np.dot(v1,r)*r
    v22=v2-2*np.dot(v2,r)*r
    return (v11[0],v11[1],v22[0],v22[1])

def update_wall_vel(vx,vy,w):#Updates velocities for wall-ball collisions
    if w==1:
        return(-vx,vy)
    else:
        return (vx,-vy)

def update_col_time(X,Y,Vx,Vy,N,b,L,t):#Updates all relevant quantities between collisions
    tplus=0
    mini=math.inf
    c1=-1
    c2=-1
    ch=0
    w=-1
    for i in range(N):#Check all ball-ball collisions
        if N==1:
            break
        for j in range(i+1,N):
            v_rel=np.array([Vx[j]-Vx[i],Vy[j]-Vy[i]])
            r_rel=np.array([X[j]-X[i],Y[j]-Y[i]])            
            tau=(1/np.linalg.norm(v_rel)**2)*(-np.dot(v_rel,r_rel)-np.sqrt(np.dot(v_rel,r_rel)**2-(np.linalg.norm(v_rel)**2)*(np.linalg.norm(r_rel**2)-4*b*b)))
            if tau<mini and tau>0:
                mini=tau
                c1=i
                c2=j
    tplus=mini            
    k=-1
    for i in range(N):#Check all wall-ball collisions
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
    if tplus==mini:#Check minimum time
        ch=1
    t=t+tplus
    b=growth(b,tplus,Vx,Vy)#Call growth function
    #Check if ball-ball or wall-ball:
    if ch==1:
        for i in range(len(X)):
            X[i]=(X[i]+Vx[i]*tplus)
            Y[i]=(Y[i]+Vy[i]*tplus)
        (Vx[c1],Vy[c1],Vx[c2],Vy[c2])=update_col_vel(b,X[c1],Y[c1],X[c2],Y[c2],Vx[c1],Vy[c1],Vx[c2],Vy[c2])
    else:
        for i in range(len(X)):
            X[i]=(X[i]+Vx[i]*tplus)
            Y[i]=(Y[i]+Vy[i]*tplus)
        Vx[k],Vy[k]=update_wall_vel(Vx[k],Vy[k],w)
    s=0#Rearrange in case of any overlaps
    with time_limit(5,'fix'):#The overlapping function must not run for more than 5 seconds. This is the stop condition.
        while(s==0):
            s=rearrange(N,X,Y,L,b)
    return (X,Y,Vx,Vy,t,b,ch)
    
        
#New growth function defined by parts. Constant growth for large collision times
#And particle distance dependent growth for small collison times
def growth(b,tplus,Vx,Vy):
        vx=min(np.abs(Vx))
        vy=min(np.abs(Vy))
        v=np.sqrt(vx**2+vy**2)
        if tplus>0.01:#0.01 defines the transition from constant growth. Change if needed
            return b+0.001#0.001 is the constant growth value. Change if needed.
        else:
            return b+v*tplus/2
    
    
        
t=0    
L=1
N=100 #No. of balls
b=0.02 #Starting radii of balls
#Initialise random starting conditions
X=np.random.rand(N)*(L-4*b)+2*b
Y=np.random.rand(N)*(L-4*b)+2*b
Vx=np.random.rand(N)*0.5
Vy=np.random.rand(N)*0.5
#Rearrange to avoid overlaps
s=0
while(s==0):
    s=rearrange(N,X,Y,L,b)
#Draw square grid
fig = mp.figure()
mp.ylim(0, 1) 
mp.xlim(0, 1) 
ax = fig.add_subplot(111)
z=0 #Counter variable
while(True):
    tem=t
    z=z+1
    ax.cla()
    time.sleep(0.2)
    (X,Y,Vx,Vy,t,b,ch)=update_col_time(X,Y,Vx,Vy,N,b,L,t)
    print(z,':','rad=',b,' col_time=',t-tem )
    for i in range(len(X)):#Draw circles
        x=X[i]
        y=Y[i]
        circle1 = mp.Circle((x, y),b , color='r')
        ax.add_artist(circle1)
    fig.canvas.draw()
    fig.canvas.flush_events()

```

Master Code:
