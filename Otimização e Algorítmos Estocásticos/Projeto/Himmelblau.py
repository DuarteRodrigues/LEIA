# Name: Beale.py
#
# Description: This script contains the execution of the optimization of the himmelblau function
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
himmelblau_expr = (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

## Compute the gradient and the hessian symbolically
# Himmelblau
grad_himmelblau = [sp.diff(himmelblau_expr, var) for var in (x1, x2)]
hess_himmelblau = [[sp.diff(g, var) for var in (x1, x2)] for g in grad_himmelblau]

## Lambdify the expressions for numerical computation
# Himmelblau
himmelblau_func = sp.lambdify((x1, x2), himmelblau_expr, 'numpy')
himmelblau_grad = sp.lambdify((x1, x2), grad_himmelblau, 'numpy')
himmelblau_hess = sp.lambdify((x1, x2), hess_himmelblau, 'numpy')

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
num_individuals = 100
num_generations = 100

h_minimum = np.array([3, 2])
h_bounds = [(-5, 5), (-5, 5)]

## Run the algorithms
# Deterministic
print("Running algorithms...")
#h_gd_history = Algorithms.gradient_descent(starting_point, himmelblau_grad, learning_rate=0.001, iterations=iterations)
#print("Gradient Descent: Done")
h_dh_history = Algorithms.downhill_simplex(starting_point, himmelblau_func, iterations=iterations)
print("Downhill: Done")
#h_nm_history = Algorithms.newton_method(starting_point, himmelblau_grad, himmelblau_hess, iterations=iterations)
#print("Newton Method: Done")
h_qn_history = Algorithms.quasi_newton(starting_point, himmelblau_func,himmelblau_grad, iterations=iterations)
print("Quasi-Newton: Done")
# Stochastic
h_sa_history = Algorithms.simulated_annealing(starting_point, himmelblau_func, iterations=iterations, initial_temp=10.0, cooling_rate=0.999, perturbation_scale=0.5)
print("Simulated Annealing: Done")
h_pso_history = Algorithms.particle_swarm_optimization(himmelblau_func, num_particles=30, iterations=iterations, bounds=h_bounds, inertia_weight=0.9, cognitive_constant=2.0, social_constant=2.0)
print("Particle Swarm Optimization: Done")
#h_ac_history = Algorithms.ant_colony_optimization(himmelblau_func, num_ants=30, iterations=200, bounds=h_bounds)
#print("Ant Colony Optimization: Done")
#h_ga_history = Algorithms.genetic_algorithm(himmelblau_func, num_individuals=num_individuals, num_generations=num_generations, bounds=h_bounds)
#print("Genetic Algorithm: Done")

## Calculate Euclidean distances
print("Calculating Euclidean Distances...")
#h_gd_distances = euclidean_distance(h_gd_history, h_minimum)
#print("Gradient Descent: Done")
h_dh_distances = euclidean_distance(h_dh_history, h_minimum)
print("Downhill: Done")
#h_nm_distances = euclidean_distance(h_nm_history, h_minimum)
#print("Newton Method: Done")
h_qn_distances = euclidean_distance(h_qn_history, h_minimum)
print("Quasi-Newton: Done")
h_sa_distances = euclidean_distance(h_sa_history, h_minimum)
print("Simulated Annealing: Done")
h_pso_distances = euclidean_distance(h_pso_history, h_minimum)
print("Particle Swarm Optimization: Done")
#h_ac_distances = euclidean_distance(h_ac_history, h_minimum)
#print("Ant Colony Optimization: Done")
#h_ga_distances = euclidean_distance(h_ga_history[0], h_minimum)
#print("Calculating Euclidean Distance: Done")

# Plot the results
plt.figure(figsize=(12, 8))
#plt.step(range(len(h_gd_distances)), h_gd_distances, where='mid', label='Gradient Descent', color='green')
plt.step(range(len(h_dh_distances)), h_dh_distances, where='mid', label='Downhill', color='blue')
#plt.step(range(len(h_nm_distances)), h_nm_distances, where='mid', label='Newton Method', color='orange')
plt.step(range(len(h_qn_distances)), h_qn_distances, where='mid', label='Quasi-Newton Method', color='purple')
plt.step(range(len(h_sa_distances)), h_sa_distances, where='mid', label='Simulated Annealing', color='red')
plt.step(range(len(h_pso_distances)), h_pso_distances, where='mid', label='Particle Swarm Optimization', color='cyan')
#plt.step(range(len(h_ac_distances)), h_ac_distances, where='mid', label='Ant Colony Optimization', color = 'maroon')
#plt.step(range(len(h_ga_distances)), h_ga_distances, where='mid', label='Genetic Algorithm', color='magenta')
plt.xlabel('Iterations')
plt.ylabel('Euclidean Distance')
plt.title('Himmelblau Function Optimization')
plt.legend()
plt.grid(True)
plt.show()