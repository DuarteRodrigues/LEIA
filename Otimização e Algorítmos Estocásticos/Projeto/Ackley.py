# Name: Beale.py
#
# Description: This script contains the execution of the optimization of the ackley function
# Author: Duarte Rodrigues - DuarteRodrigues @github
#         Ecleber Monteiro
# Student ID: a22206488/a22210899
# Date: June 2024
# Subject: Algoritmos Estocásticos e Otimização

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from sympy import exp, sqrt, cos, pi

import Algorithms

# Define the point's coordinates and their symbol
x1, x2 = sp.symbols('x1 x2')

# Define the expressions of each function
ackley_expr = -20 * exp(-0.2 * sqrt(0.5 * (x1**2 + x2**2))) + (-exp(0.5 * (cos(2*pi*x1) + cos(2*pi*x2)))) + 20 + exp(1)

## Compute the gradient and the hessian symbolically
# Ackley
grad_ackley = [sp.diff(ackley_expr, var) for var in (x1,x2)]
hess_ackley = [[sp.diff(g, var) for var in (x1, x2)] for g in grad_ackley]

## Lambdify the expressions for numerical computation
ackley_func = sp.lambdify((x1, x2), ackley_expr, 'numpy')
ackley_grad = sp.lambdify((x1, x2), grad_ackley, 'numpy')
ackley_hess = sp.lambdify((x1, x2), hess_ackley, 'numpy')

# Euclidean distance calculation
def euclidean_distance(history, minimum):
    """
    Function that calculates the euclidean distance between the current
    location and the minimum location.

    Parameters
    ----------
    history (array-like): Array with the history of the location.
    minimum (array-like): Array with the minimum location.

    Returns
    -------
    distance (float): The euclidean distance between the current location
    and the minimum location.
    """
    return np.sqrt((history[:, 0] - minimum[0])**2 + (history[:, 1] - minimum[1])**2)

# Main script
starting_point = np.array([1, 1])
iterations = 1000
num_individuals = 50
num_generations = 100

a_minimum = np.array([0, 0])
a_bounds = [(-5, 5), (-5, 5)]

## Run the algorithms
# Deterministic
print("Running algorithms...")
#a_gd_history = Algorithms.gradient_descent(starting_point, ackley_grad, learning_rate=0.001, iterations=iterations)
#print("Gradient Descent: Done")
a_dh_history = Algorithms.downhill_simplex(starting_point, ackley_func, iterations=iterations)
print("Downhill: Done")
#a_nm_history = Algorithms.newton_method(starting_point, ackley_grad, ackley_hess, iterations=iterations)
#print("Newton Method: Done")
a_qn_history = Algorithms.quasi_newton(starting_point, ackley_func, ackley_grad, iterations=iterations)
print("Quasi-Newton: Done")
# Stochastic
#a_sa_history = Algorithms.simulated_annealing(starting_point, ackley_func, iterations=iterations, initial_temp=10.0, cooling_rate=0.999, perturbation_scale=0.5)
#print("Simulated Annealing: Done")
a_pso_history = Algorithms.particle_swarm_optimization(ackley_func, num_particles=30, iterations=iterations, bounds=a_bounds, inertia_weight=0.9, cognitive_constant=2.0, social_constant=2.0)
print("Particle Swarm Optimization: Done")
a_ac_history = Algorithms.ant_colony_optimization(ackley_func, num_ants=30, iterations=200, bounds=a_bounds)
print("Ant Colony Optimization: Done")
#a_ga_history = Algorithms.genetic_algorithm(ackley_func, num_individuals=num_individuals, num_generations=num_generations, bounds=a_bounds)
#print("Genetic Algorithm: Done")

## Calculate Euclidean distances
print("Calculating Euclidean Distances...")
#a_gd_distances = euclidean_distance(a_gd_history, a_minimum)
#print("Gradient Descent: Done")
a_dh_distances = euclidean_distance(a_dh_history, a_minimum)
print("Downhill: Done")
#a_nm_distances = euclidean_distance(a_nm_history, a_minimum)
#print("Newton Method: Done")
a_qn_distances = euclidean_distance(a_qn_history, a_minimum)
print("Quasi-Newton: Done")
#a_sa_distances = euclidean_distance(a_sa_history, a_minimum)
#print("Simulated Annealing: Done")
a_pso_distances = euclidean_distance(a_pso_history, a_minimum)
print("Particle Swarm Optimization: Done")
a_ac_distances = euclidean_distance(a_ac_history, a_minimum)
print("Ant Colony Optimization: Done")
#a_ga_distances = euclidean_distance(a_ga_history[0], a_minimum)
#print("Calculating Euclidean Distance: Done")

# Plot the results
plt.figure(figsize=(12, 8))
#plt.step(range(len(a_gd_distances)), a_gd_distances, where='mid', label='Gradient Descent', color='green')
plt.step(range(len(a_dh_distances)), a_dh_distances, where='mid', label='Downhill', color='blue')
#plt.step(range(len(a_nm_distances)), a_nm_distances, where='mid', label='Newton Method', color='orange')
plt.step(range(len(a_qn_distances)), a_qn_distances, where='mid', label='Quasi-Newton Method', color='purple')
#plt.step(range(len(a_sa_distances)), a_sa_distances, where='mid', label='Simulated Annealing', color='red')
plt.step(range(len(a_pso_distances)), a_pso_distances, where='mid', label='Particle Swarm Optimization', color='cyan')
plt.step(range(len(a_ac_distances)), a_ac_distances, where='mid', label='Ant Colony Optimization', color = 'maroon')
#plt.step(range(len(a_ga_distances)), a_ga_distances, where='mid', label='Genetic Algorithm', color='magenta')
plt.xlabel('Iterations')
plt.ylabel('Euclidean Distance')
plt.title('Ackley Function Optimization')
plt.legend()
plt.grid(True)
plt.show()