import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Define symbols
x1, x2 = sp.symbols('x1 x2')

# Define functions and their expressions
himmelblau_expr = (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2
beale_expr = (1.5 - x1 + x1 * x2)**2 + (2.25 - x1 + x1 * x2**2)**2 + (2.625 - x1 + x1 * x2**3)**2

# Compute gradients and Hessians symbolically
himmelblau_func = sp.lambdify((x1, x2), himmelblau_expr, 'numpy')
himmelblau_grad = sp.lambdify((x1, x2), sp.Matrix([himmelblau_expr.diff(x1), himmelblau_expr.diff(x2)]), 'numpy')
himmelblau_hess = sp.lambdify((x1, x2), sp.hessian(himmelblau_expr, (x1, x2)), 'numpy')

beale_grad = sp.lambdify((x1, x2), sp.Matrix([beale_expr.diff(x1), beale_expr.diff(x2)]), 'numpy')
beale_hess = sp.lambdify((x1, x2), sp.hessian(beale_expr, (x1, x2)), 'numpy')

# Ant Colony Optimization algorithm
def ant_colony_optimization(func, num_ants, iterations, bounds, evaporation_rate=0.1, alpha=1, beta=2, num_neighbors=5):
    num_dimensions = len(bounds)
    bounds = np.array(bounds)
    pheromones = np.ones((100, 100))
    best_solution = None
    best_score = np.inf
    history = []

    def heuristic(x):
        return 1.0 / (func(*x) + 1e-10)
    
    def get_probability(x):
        x_int = np.clip((x - bounds[:, 0]) / (bounds[:, 1] - bounds[:, 0]) * 99, 0, 99).astype(int)
        return pheromones[x_int[0], x_int[1]] ** alpha * heuristic(x) ** beta

    for iteration in range(iterations):
        all_ants = []
        for _ in range(num_ants):
            x = np.random.rand(num_dimensions) * (bounds[:, 1] - bounds[:, 0]) + bounds[:, 0]
            path = [x.copy()]
            for _ in range(100):
                neighbors = [x + np.random.randn(num_dimensions) for _ in range(num_neighbors)]
                neighbors = np.clip(neighbors, bounds[:, 0], bounds[:, 1])
                probabilities = np.array([get_probability(neighbor) for neighbor in neighbors])
                probabilities /= probabilities.sum()
                x = neighbors[np.random.choice(range(len(neighbors)), p=probabilities)]
                path.append(x.copy())
            all_ants.append((path, func(*x)))
            if func(*x) < best_score:
                best_score = func(*x)
                best_solution = x

        history.append(best_solution.copy())
        pheromones *= (1 - evaporation_rate)
        for path, score in all_ants:
            for point in path:
                point = np.clip((point - bounds[:, 0]) / (bounds[:, 1] - bounds[:, 0]) * 99, 0, 99).astype(int)
                pheromones[int(point[0]), int(point[1])] += 1.0 / (score + 1e-10)

        # Print progress every 100 iterations
        if (iteration + 1) % 100 == 0:
            print(f"Iteration {iteration + 1}/{iterations}, Best Score: {best_score}")

    return np.array(history)

# Euclidean distance calculation
def euclidean_distance(history, minimum):
    return np.sqrt(np.sum((history - minimum)**2, axis=1))

# Define bounds and minimum for Himmelblau function
h_minimum = np.array([3, 2])
h_bounds = [(-5, 5), (-5, 5)]

# Run Ant Colony Optimization on Himmelblau function
print("Running Ant Colony Optimization...")
h_ac_history = ant_colony_optimization(himmelblau_func, num_ants=5, iterations=100, bounds=h_bounds)
print("Ant Colony Optimization: Done")

# Calculate Euclidean distances from minimum
print("Calculating Euclidean Distances...")
h_ac_distances = euclidean_distance(h_ac_history, h_minimum)
print("Euclidean Distances: Done")

# Plot the results
plt.figure(figsize=(12, 8))
plt.step(range(len(h_ac_distances)), h_ac_distances, where='mid', label='Ant Colony Optimization', color='maroon')
plt.xlabel('Iterations')
plt.ylabel('Euclidean Distance')
plt.title('Himmelblau Function Optimization using Ant Colony Optimization')
plt.legend()
plt.grid(True)
plt.show()