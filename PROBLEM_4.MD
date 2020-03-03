PROBLEM 3: CREATE A CIRCLE ON THE SPHERE

IDEAS:
- Fluffy boi
-
-

Julianna's Code here:

Li Ting's Code here:

Marcus' Code here:

Suraj's Code here:
```python
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from spherical_geometry import polygon
from spherical_geometry import vector
radius=np.pi/2 # Radius of circle
C=polygon.SphericalPolygon.from_cone(vector.vector_to_lonlat(1,0,0)[0],vector.vector_to_lonlat(1,0,0)[1],radius,degrees=False)
print(C.area())#Results is area of circle with radius pi/2 which is a hemisphere.
```
Geraldine's Code here:

Master Code here:
