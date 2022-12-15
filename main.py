import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rotateFunction


class hyperboloid:
    x = np.arange(-5, 5, 0.2)
    y = np.arange(-5, 5, 0.2)
    z = 0
    a = 1
    b = 1
    c = 1
    angle = 0
    def __init__(self, a=1, b=1, c=1, angle=0):
        self.a = a
        self.b = b
        self.c = c
        self.angle = angle
        self.x, self.y = np.meshgrid(self.x, self.y)
        self.z = np.sqrt(c**2 * (1 + self.x**2/a**2 + self.y**2/b**2))
        self.x, self.y, self.z = rotateFunction.rotate_function((0,0,0), (0,1,0), self.x, self.y, self.z, angle)

def show(hb1, hb2, size):
    fig = plt.figure(figsize=(size, size))
    ax_3d = fig.add_subplot(projection='3d')
    ax_3d.plot_wireframe(hb1.x, hb1.y, hb1.z, color = 'g')
    ax_3d.plot_wireframe(hb2.x, hb2.y, hb2.z, color = 'r')
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    plt.show()


def main():
    fig1 = hyperboloid(1, 1, 1, 0)
    fig2 = hyperboloid(1, 1, 1, np.pi/4)
    show(fig1, fig2, 10)


if __name__ == '__main__':
    main()