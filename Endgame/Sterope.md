```
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random as rdm
import pickle as pick
import matplotlib

print(matplotlib.get_backend())

test=pick.load(open("Succ Iter (543) Runs (1)","rb"))
test[0].text(0.35,0.75,'Packing fraction achieved: '+str(test[1]*100)+'%')
test[0].show()
```
