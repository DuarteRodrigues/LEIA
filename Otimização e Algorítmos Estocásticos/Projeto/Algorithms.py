# Name: Algorithms.py
#
# Description: This script contains various algorithms for optimization of different functions
# Author: Duarte Rodrigues - DuarteRodrigues @github
#         Ecleber Monteiro
# Student ID: a22206488/a22210899
# Date: June 2024
# Subject: Algoritmos Estocásticos e Otimização

import numpy as np

# Deterministic Algorithm - Gradient Descent 
def gradient_descent(starting_point, grad_func, learning_rate, iterations):
    """
    Perform gradient descent optimization.

    Parameters:
    starting_point (array-like): Initial point to start the gradient descent.
    grad_func (function): Function that computes the gradient at a given point.
    learning_rate (float): Step size for each iteration.
    iterations (int): Number of iterations to perform.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
    x = starting_point
    history = [x]
    for _ in range(iterations):
        grad = np.array(grad_func(*x))
        x = x - learning_rate * grad
        history.append(x)
    return np.array(history)

# Deterministic Algorithm - Downhill Simplex (Nelder-Mead) 
def downhill_simplex(starting_point, func, iterations):
    """
    Perform downhill simplex optimization.

    Parameters:
    starting_point (array-like): Initial point to start the gradient descent.
    func (function): Function that computes the mathematical function at a given point.
    iterations (int): Number of iterations to perform.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
    n = len(starting_point)
    simplex = np.array([starting_point + np.random.rand(n) for _ in range(n + 1)])
    history = [simplex.mean(axis=0)]
    alpha, gamma, rho, sigma = 1.0, 2.0, 0.5, 0.5

    for _ in range(iterations):
        simplex = sorted(simplex, key=lambda x: func(*x))
        centroid = np.mean(simplex[:-1], axis=0)
        xr = centroid + alpha * (centroid - simplex[-1])
        if func(*simplex[0]) <= func(*xr) < func(*simplex[-2]):
            simplex[-1] = xr
        elif func(*xr) < func(*simplex[0]):
            xe = centroid + gamma * (xr - centroid)
            simplex[-1] = xe if func(*xe) < func(*xr) else xr
        else:
            xc = centroid + rho * (simplex[-1] - centroid)
            if func(*xc) < func(*simplex[-1]):
                simplex[-1] = xc
            else:
                simplex = simplex[0] + sigma * (simplex - simplex[0])
        history.append(np.mean(simplex, axis=0))
    return np.array(history)

# Deterministic Algorithm - Newton's Method
def newton_method(starting_point, grad_func, hess_func, iterations):
    """
    Perform newton method optimization.

    Parameters:
    starting_point (array-like): Initial point to start the gradient descent.
    grad_func (function): Function that computes the gradient at a given point.
    hess_func (function): Function that computes the hessian at a given point.
    learning_rate (float): Step size for each iteration.
    iterations (int): Number of iterations to perform.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
    x = np.array(starting_point, dtype=float)
    history = [x.copy()]
    for _ in range(iterations):
        grad = np.array(grad_func(*x))
        hess = np.array(hess_func(*x))
        x -= np.linalg.inv(hess).dot(grad)
        history.append(x.copy())
    
    return np.array(history)

# Deterministic Algorithm - Quasi-Newton Method
def quasi_newton(starting_point, func, grad_func, iterations):
    """
    Perform quasi-newton optimization.

    Parameters:
    starting_point (array-like): Initial point to start the gradient descent.
    func (function): Function that computes the mathematical function at a given point.
    grad_func (function): Function that computes the gradient at a given point.
    iterations (int): Number of iterations to perform.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
    x = np.array(starting_point, dtype=float)
    n = len(x)
    I = np.eye(n)
    H = I
    history = [x.copy()]

    for _ in range(iterations):
        grad = np.array(grad_func(*x))
        p = -H.dot(grad)
        alpha = 1.0
        while func(*(x + alpha * p)) > func(*x) + 0.1 * alpha * grad.dot(p):
            alpha *= 0.8
        x_new = x + alpha * p
        s = x_new - x
        y = np.array(grad_func(*x_new)) - grad
        if np.dot(y, s) != 0:  # Avoid division by zero
            rho = 1.0 / np.dot(y, s)
            H = (I - rho * np.outer(s, y)).dot(H).dot(I - rho * np.outer(y, s)) + rho * np.outer(s, s)
        x = x_new
        history.append(x.copy())
    return np.array(history)

# Stochastic Algorithm - Simulated Annealing
def simulated_annealing(starting_point, func, iterations, initial_temp, cooling_rate, perturbation_scale=1.0):
    """
    Perform simulated annealing optimization.

    Parameters:
    starting_point (array-like): Initial point to start the gradient descent.
    func (function): Function that computes the mathematical function at a given point.
    iterations (int): Number of iterations to perform.
    initial_temp (float): Indicator of the temperature at the beginning of the process.
    cooling_rate (float): Rate at which the temperature decreases.
    perturbation_scale (float): Scale of the perturbations applied during the process.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
    x = starting_point
    history = [x]
    current_temp = initial_temp
    for i in range(iterations):
        next_x = x + np.random.normal(0, perturbation_scale, len(x))
        delta_e = func(*next_x) - func(*x)
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / current_temp):
            x = next_x
        current_temp *= cooling_rate
        history.append(x)
    return np.array(history)

# Stochastic Algorithm - Particle Swarm Optimization
def particle_swarm_optimization(func, num_particles, iterations, bounds, inertia_weight=0.9, cognitive_constant=2.0, social_constant=2.0):
    """
    Perform particle swarm optimization.

    Parameters:
    func (function): Function that computes the mathematical function at a given point.
    num_particles (int): Number of particles in the swarm.
    iterations (int): Number of iterations to perform.
    bounds (list): List of tuples representing the lower and upper bounds of each dimension.
    inertia_weight (float, optional): Inertia weight. Defaults to 0.9.
    cognitive_constant (float, optional): Cognitive constant. Defaults to 2.0.
    social_constant (float, optional): Social constant. Defaults to 2.0.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
    num_dimensions = len(bounds)
    particles = np.random.rand(num_particles, num_dimensions)
    for i in range(num_dimensions):
        particles[:, i] = bounds[i][0] + particles[:, i] * (bounds[i][1] - bounds[i][0])
    
    velocities = np.random.rand(num_particles, num_dimensions)
    personal_best_positions = particles.copy()
    personal_best_scores = np.array([func(*p) for p in particles])
    global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    
    history = [global_best_position.copy()]

    for t in range(iterations):
        inertia_weight_t = inertia_weight * (1 - t / iterations)  # Linearly decreasing inertia weight
        for i in range(num_particles):
            velocities[i] = (
                inertia_weight_t * velocities[i]
                + cognitive_constant * np.random.rand() * (personal_best_positions[i] - particles[i])
                + social_constant * np.random.rand() * (global_best_position - particles[i])
            )
            particles[i] += velocities[i]
            particles[i] = np.clip(particles[i], [b[0] for b in bounds], [b[1] for b in bounds])
            score = func(*particles[i])
            if score < personal_best_scores[i]:
                personal_best_scores[i] = score
                personal_best_positions[i] = particles[i]
        global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
        history.append(global_best_position.copy())
    
    return np.array(history)

# Stochastic Algorithms - Ant Colony Optimization
def ant_colony_optimization(func, num_ants, iterations, bounds, evaporation_rate=0.1, alpha=1, beta=2, num_neighbors = 5):
    """
    Perform ant colony optimization.

    Parameters:
    func (function): Function that computes the mathematical function at a given point.
    num_ants (int): Number of ants to use in the optimization.
    iterations (int): Number of iterations to perform.
    bounds (list): List of tuples representing the lower and upper bounds of each dimension.
    evaporation_rate (float, optional): Rate at which pheromones evaporate. Defaults to 0.1.
    alpha (int, optional): Importance of pheromones. Defaults to 1.
    beta (int, optional): Importance of heuristic information. Defaults to 2.
    num_neighbors (int, optional): Number of neighbors to consider. Defaults to 5.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
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

# Stochastic Algorithms - Genetic Algorithm
def genetic_algorithm(func, num_individuals, num_generations, bounds):
    """
    Perform genetic algorithm optimization.

    Parameters:
    func (function): Function that computes the mathematical function at a given point.
    num_individuals (int): Number of individuals in the population.
    num_generations (int): Number of generations to evolve.
    bounds (list): List of tuples representing the lower and upper bounds of each dimension.

    Returns:
    numpy.ndarray: Array of points representing the history of the optimization process.
    """
    num_dimensions = len(bounds)
    population = np.random.rand(num_individuals, num_dimensions)
    for i in range(num_dimensions):
        population[:, i] = bounds[i][0] + population[:, i] * (bounds[i][1] - bounds[i][0])

    history = [population.copy()]

    for _ in range(num_generations):
        # Evaluate the fitness of each individual
        fitness = np.array([func(*ind) for ind in population])

        # Select parents based on fitness (roulette wheel selection)
        probabilities = fitness / np.sum(fitness)
        selected_indices = np.random.choice(num_individuals, size=num_individuals, p=probabilities)
        parents = population[selected_indices]

        # Crossover (single point crossover)
        crossover_point = np.random.randint(1, num_dimensions)
        offspring = []
        for i in range(0, num_individuals, 2):
            parent1, parent2 = parents[i], parents[i+1]
            child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
            offspring.extend([child1, child2])
        offspring = np.array(offspring)
        
        # Mutation (random reset mutation)
        mutation_rate = 0.1
        for i in range(num_individuals):
            if np.random.rand() < mutation_rate:
                mutate_index = np.random.randint(num_dimensions)
                offspring[i, mutate_index] = bounds[mutate_index][0] + np.random.rand() * (bounds[mutate_index][1] - bounds[mutate_index][0])
        
        # Replace population with offspring
        population = offspring.copy()
        history.append(population.copy())
    
    return np.array(history)