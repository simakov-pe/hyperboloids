import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.tri import Triangulation

u = np.linspace(0, 2*np.pi, 20)
v = u.copy()
u, v = np.meshgrid(u, v)

x = np.ravel(np.sinh(u)*np.cos(v))
y = np.ravel(np.sinh(u)*np.sin(v))
z = np.ravel(np.cosh(u))

tri = Triangulation(np.ravel(u), np.ravel(v))


ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap='jet', antialiased=True)

plt.show()