# Name: Beale.py
#
# Description: This script contains the execution of the optimization of the beale function
# Author: Duarte Rodrigues - DuarteRodrigues @github
#         Ecleber Monteiro
# Student ID: a22206488/a22210899
# Date: June 2024
# Subject: Algoritmos Estocásticos e Otimização

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

import Algorithms

# Define the point's coordinates and their symbol
x1, x2 = sp.symbols('x1 x2')

# Define the expressions of each function
beale_expr = (1.5 - x1 + x1 * x2)**2 + (2.25 - x1 + x1 * x2**2)**2 + (2.625 - x1 + x1 * x2**3)**2

## Compute the gradient and the hessian symbolically
# Beale
grad_beale = [sp.diff(beale_expr, var) for var in (x1, x2)]
hess_beale = [[sp.diff(g, var) for var in (x1, x2)] for g in grad_beale]

## Lambdify the expressions for numerical computation
# Beale
beale_func = sp.lambdify((x1, x2), beale_expr, 'numpy')
beale_grad = sp.lambdify((x1, x2), grad_beale, 'numpy')
beale_hess = sp.lambdify((x1, x2), hess_beale, 'numpy')

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
iterations = 10000
num_individuals = 50
num_generations = 100

b_minimum = np.array([3, 0.5])
b_bounds = [(-4.5, 4.5), (-4.5, 4.5)]

## Run the algorithms
# Deterministic
print("Running algorithms...")
#b_gd_history = Algorithms.gradient_descent(starting_point, beale_grad, learning_rate=0.001, iterations=iterations)
#print("Gradient Descent: Done")
b_dh_history = Algorithms.downhill_simplex(starting_point, beale_func, iterations=iterations)
print("Downhill: Done")
#b_nm_history = Algorithms.newton_method(starting_point, beale_grad, beale_hess, iterations=iterations)
#print("Newton Method: Done")
b_qn_history = Algorithms.quasi_newton(starting_point, beale_func,beale_grad, iterations=iterations)
print("Quasi-Newton: Done")
# Stochastic
#b_sa_history = Algorithms.simulated_annealing(starting_point, beale_func, iterations=iterations, initial_temp=10.0, cooling_rate=0.999, perturbation_scale=0.5)
#print("Simulated Annealing: Done")
b_pso_history = Algorithms.particle_swarm_optimization(beale_func, num_particles=30, iterations=iterations, bounds=b_bounds, inertia_weight=0.9, cognitive_constant=2.0, social_constant=2.0)
print("Particle Swarm Optimization: Done")
b_ac_history = Algorithms.ant_colony_optimization(beale_func, num_ants=30, iterations=200, bounds=b_bounds)
print("Ant Colony Optimization: Done")
#b_ga_history = Algorithms.genetic_algorithm(beale_func, num_individuals=num_individuals, num_generations=num_generations, bounds=b_bounds)
#print("Genetic Algorithm: Done")

## Calculate Euclidean distances
print("Calculating Euclidean Distances...")
#b_gd_distances = euclidean_distance(b_gd_history, b_minimum)
#print("Gradient Descent: Done")
b_dh_distances = euclidean_distance(b_dh_history, b_minimum)
print("Downhill: Done")
#b_nm_distances = euclidean_distance(b_nm_history, b_minimum)
#print("Newton Method: Done")
b_qn_distances = euclidean_distance(b_qn_history, b_minimum)
print("Quasi-Newton: Done")
#b_sa_distances = euclidean_distance(b_sa_history, b_minimum)
#print("Simulated Annealing: Done")
b_pso_distances = euclidean_distance(b_pso_history, b_minimum)
print("Particle Swarm Optimization: Done")
b_ac_distances = euclidean_distance(b_ac_history, b_minimum)
print("Ant Colony Optimization: Done")
#b_ga_distances = euclidean_distance(b_ga_history[0], b_minimum)
#print("Calculating Euclidean Distance: Done")

# Plot the results
plt.figure(figsize=(12, 8))
#plt.step(range(len(b_gd_distances)), b_gd_distances, where='mid', label='Gradient Descent', color='green')
plt.step(range(len(b_dh_distances)), b_dh_distances, where='mid', label='Downhill', color='blue')
#plt.step(range(len(b_nm_distances)), b_nm_distances, where='mid', label='Newton Method', color='orange')
plt.step(range(len(b_qn_distances)), b_qn_distances, where='mid', label='Quasi-Newton Method', color='purple')
#plt.step(range(len(b_sa_distances)), b_sa_distances, where='mid', label='Simulated Annealing', color='red')
plt.step(range(len(b_pso_distances)), b_pso_distances, where='mid', label='Particle Swarm Optimization', color='cyan')
plt.step(range(len(b_ac_distances)), b_ac_distances, where='mid', label='Ant Colony Optimization', color = 'maroon')
#plt.step(range(len(b_ga_distances)), b_ga_distances, where='mid', label='Genetic Algorithm', color='magenta')
plt.xlabel('Iterations')
plt.ylabel('Euclidean Distance')
plt.title('Beale Function Optimization')
plt.legend()
plt.grid(True)
plt.show()