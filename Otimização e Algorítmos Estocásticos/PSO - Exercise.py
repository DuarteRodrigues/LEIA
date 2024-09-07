import numpy as np
from scipy.integrate import quad
from pyswarm import pso

def objective_function(vars):
    x, y = vars

    integrand = lambda x: 3*x + 2*y

    integral_value, _ = quad(integrand, 0, x)

    a = 1
    v = 1

    f_value = np.exp(-(a**2 + v**2) + 5) *integral_value

    return -f_value

lb = [0, 0]
ub = [10, 10]


x_opt, f_opt = pso(objective_function, lb, ub)

print("Optimal solution (x, y):", x_opt)
print("Maximum value of f(x, y):", -f_opt)