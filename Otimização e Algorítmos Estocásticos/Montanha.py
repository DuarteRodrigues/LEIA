import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return x**2 + y**2

x = np.linspace(-5,5,300)
y = np.linspace(-5,5,300)
X, Y = np.meshgrid(x,y)
Z = f(X,Y)

fig= plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()