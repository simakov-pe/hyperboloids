import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(10, 10))
ax_3d = fig.add_subplot(projection='3d')
x = np.arange(-5, 5, 0.2)
y = np.arange(-5, 5, 0.2)
x, y = np.meshgrid(x, y)
a = 1
b = 1
c = 1
alpha = np.pi/3
z1 = np.sqrt(c**2 * (((x*np.cos(alpha) - y*np.sin(alpha))**2/a**2) + ((x*np.sin(alpha) + y*np.cos(alpha))**2/b**2) + 1))
z2 = -z1
ax_3d.plot_surface(x, y, z1, color='g')
ax_3d.plot_surface(x, y, z2, color='g')


ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

plt.show()