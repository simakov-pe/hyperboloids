import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rotateFunction

class surface:
    x = np.arange(-5, 5, 0.2)
    y = np.arange(-5, 5, 0.2)
    z1 = 0
    z2 = 0
    l1 = 1
    l2 = 1
    l3 = 1
    k4 = 1
    i3 = 1
    angle = 0

    def __init__(self, l1=1, l2=0, l3=0, k4=1, i3=1, angle=0):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.k4 = k4
        self.i3 = i3
        self.x, self.y = np.meshgrid(self.x, self.y)
        self.z1 = np.sqrt(abs((-l1*self.x**2/l3) + (-l2*self.y**2/l3) + (-k4/(i3*l3))))
        self.z2 = -self.z1
        self.x, self.y, self.z1 = rotateFunction.rotate_function((0, 0, 0), (0, 1, 0), self.x, self.y, self.z1, angle)
        self.x, self.y, self.z2 = rotateFunction.rotate_function((0, 0, 0), (0, 1, 0), self.x, self.y, self.z2, angle)

    def show(self, fig2=None, size=10):
        fig = plt.figure(figsize=(size, size))
        ax_3d = fig.add_subplot(projection='3d')
        ax_3d.plot_wireframe(self.x, self.y, self.z1, color='g')
        ax_3d.plot_wireframe(self.x, self.y, self.z2, color='g')
        if fig2 != None:
            ax_3d.plot_wireframe(fig2.x, fig2.y, fig2.z1, color='r')
            ax_3d.plot_wireframe(fig2.x, fig2.y, fig2.z2, color='r')
        ax_3d.set_xlabel('x')
        ax_3d.set_ylabel('y')
        ax_3d.set_zlabel('z')
        plt.show()

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
    def show(self, hb2=None, size=10):
        fig = plt.figure(figsize=(size, size))
        ax_3d = fig.add_subplot(projection='3d')
        ax_3d.plot_wireframe(self.x, self.y, self.z, color='g')
        if hb2 != None:
            ax_3d.plot_wireframe(hb2.x, hb2.y, hb2.z, color='r')
        ax_3d.set_xlabel('x')
        ax_3d.set_ylabel('y')
        ax_3d.set_zlabel('z')
        plt.show()


def main():
    # hb1 = hyperboloid(1, 1, 1, 0)
    # hb2 = hyperboloid(1, 1, 1, np.pi/4)
    # show(hb1, hb2, 10)

    fig1 = surface(1, 1, -1, 1, 1, 0)
    fig2 = surface(1, 1, -5, -5, 1, 0)
    fig1.show(fig2, 10)

if __name__ == '__main__':
   main()