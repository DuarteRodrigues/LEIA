import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
    return (x-3)**2 + (y+2)**2

def df_dx(x):
    return 2*(x-3)

def df_dy(y):
    return 2*(y+2)

def gradient_descent(learning_rate, initial_guess, num_iterations):
    x, y = initial_guess
    history = [(x,y)] # Lista para armazenar o histórico das posições x,y durante a otimização
    while((np.sqrt(x**2+y**2))<00000.1):
        gradient_x = df_dx(x,y)
        gradient_y = df_dy(x,y)
        x = x - learning_rate * gradient_x
        y = y - learning_rate * gradient_y
        history.append((x,y))
    return (x,y), history

learning_rate = 0.1
initial_guess = (2,3)
num_iterations = 10

minimizer, history = gradient_descent(learning_rate, initial_guess, num_iterations)

x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = f(X,Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)
ax.scatter([x for x, _ in history], [y for _, y in history], [f(x,y) for x, y in history], color='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
ax.set_title('Gradient Descent Optimization for f(x,y)')

plt.show()
print("Minimum value of f(x,y) found by gradient descent", f(*minimizer))
print("Value of x at the minimum:", minimizer[0])
print("Value of y at the minimum:", minimizer[1])