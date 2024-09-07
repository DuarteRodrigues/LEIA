import numpy as np
import matplotlib.pyplot as plt

def himmelblau(point):
    x, y = point
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def himmelblau_grad(point):
    x, y = point
    dfdx = 4 * x * (x**2 + y - 11) + 2 * (x + y**2 - 7)
    dfdy = 2 * (x**2 + y - 11) + 4 * y * (x + y**2 - 7)
    return [dfdx, dfdy]

def gradient_descent(grad_func, initial_point, learning_rate = 0.01, iterations = 1000):
    point = np.array(initial_point, dtype=float)
    history = [point.copy()]

    for _ in range(iterations):
        grad = np.array(grad_func(point))
        point -= learning_rate * grad
        history.append(point.copy())

    return np.array(history)

initial_point = [6, 6]
history = gradient_descent (himmelblau_grad, initial_point, 0.01, 10000)

def plot_history(history, title):
    history = np.array(history)
    distances = np.linalg.norm(history - np.array([3, 2]), axis = 1)
    plt.plot(distances)
    plt.title(title)
    plt.xlabel("Iterações")
    plt.ylabel("Distância ao ótimo")
    plt.show()

plot_history(history, "Gradient Descent - Himmelblau")