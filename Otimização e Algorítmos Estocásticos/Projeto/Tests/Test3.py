import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from math import exp, sqrt, cos, pi, sin

# Define the point's coordinates and their symbol
x1, x2 = sp.symbols('x1 x2')

# Define the expressions of each function
himmelblau_expr = (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2
beale_expr = (1.5 - x1 + x1 * x2)**2 + (2.25 - x1 + x1 * x2**2)**2 + (2.625 - x1 + x1 * x2**3)**2
#ackley_expr = -20 * exp(-0.2 * sqrt(0.5 * (x1**2 + x2**2))) + (-exp(0.5 * (cos(2*pi*x1) + cos(2*pi*x2)))) + 20 + exp(1)

## Compute the gradient and the hessian symbolically
# Himmelblau
grad_himmelblau = [sp.diff(himmelblau_expr, var) for var in (x1, x2)]
hess_himmelblau = [[sp.diff(g, var) for var in (x1, x2)] for g in grad_himmelblau]

# Beale
grad_beale = [sp.diff(beale_expr, var) for var in (x1, x2)]
hess_beale = [[sp.diff(g, var) for var in (x1, x2)] for g in grad_beale]

# Ackley
#grad_ackley = [sp.diff(ackley_expr, var) for var in (x1,x2)]
#hess_ackley = [[sp.diff(g, var) for var in (x1, x2)] for g in grad_ackley]

## Lambdify the expressions for numerical computation
# Himmelblau
himmelblau_func = sp.lambdify((x1, x2), himmelblau_expr, 'numpy')
himmelblau_grad = sp.lambdify((x1, x2), grad_himmelblau, 'numpy')
himmelblau_hess = sp.lambdify((x1, x2), hess_himmelblau, 'numpy')

# Beale
beale_func = sp.lambdify((x1, x2), beale_expr, 'numpy')
beale_grad = sp.lambdify((x1, x2), grad_beale, 'numpy')
beale_hess = sp.lambdify((x1, x2), hess_beale, 'numpy')

# Ackley
#ackley_func = sp.lambdify((x1, x2), ackley_expr, 'numpy')
#ackley_grad = sp.lambdify((x1, x2), grad_ackley, 'numpy')
#ackley_hess = sp.lambdify((x1, x2), hess_ackley, 'numpy')

# Deterministic Algorithm - Gradient Descent 
def gradient_descent(starting_point, grad_func, learning_rate, iterations):
    x = starting_point
    history = [x]
    for _ in range(iterations):
        grad = np.array(grad_func(*x))
        x = x - learning_rate * grad
        history.append(x)
    return np.array(history)

# Deterministic Algorithm - Downhill Simplex (Nelder-Mead) 
def downhill_simplex(starting_point, func, iterations):
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
    x = np.array(starting_point, dtype=float)
    history = [x.copy()]
    for _ in range(iterations):
        grad = np.array(grad_func(*x))
        hess = np.array(hess_func(*x))
        x -= np.linalg.inv(hess).dot(grad)
        history.append(x.copy())
    return np.array(history)

# Deterministic Algorithm - Quasi-Newton Method
def quasi_newton(starting_point, func ,grad_func, iterations):
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
def simulated_annealing(starting_point, func, iterations, initial_temp, cooling_rate):
    x = starting_point
    history = [x]
    current_temp = initial_temp
    for i in range(iterations):
        next_x = x + np.random.normal(0, 1, 2)
        delta_e = func(*next_x) - func(*x)
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / current_temp):
            x = next_x
        current_temp *= cooling_rate
        history.append(x)
    return np.array(history)

# Stochastic Algorithm - Particle Swarm Optimization
def particle_swarm_optimization(func, num_particles, iterations, bounds, inertia_weight=0.7, cognitive_constant=1.5, social_constant=1.5):
    num_dimensions = len(bounds)
    particles = np.random.rand(num_particles, num_dimensions)
    for i in range(num_dimensions):
        particles[:, i] = bounds[i][0] + particles[:, i] * (bounds[i][1] - bounds[i][0])
    
    velocities = np.zeros_like(particles)
    personal_best_positions = particles.copy()
    personal_best_scores = np.array([func(*p) for p in particles])
    global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    
    history = [global_best_position.copy()]

    for _ in range(iterations):
        for i in range(num_particles):
            velocities[i] = (
                inertia_weight * velocities[i]
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

# Euclidean distance calculation
def euclidean_distance(history, minimum):
    return np.sqrt((history[:, 0] - minimum[0])**2 + (history[:, 1] - minimum[1])**2)

# Main script
starting_point = np.array([1, 1])
iterations = 10000
num_individuals = 50
num_generations = 100

h_minimum = np.array([3, 2])
b_minimum = np.array([3, 0.5])
a_minimum = np.array([0, 0])

h_bounds = [(-5, 5), (-5, 5)]
b_bounds = [(-4.5, 4.5), (-4.5, 4.5)]
a_bounds = [(-5, 5), (-5, 5)]

## Run the algorithms
# Deterministic
print("Running algorithms...")
h_gd_history = gradient_descent(starting_point, himmelblau_grad, learning_rate=0.001, iterations=iterations)
print("Gradient Descent: Done")
h_dh_history = downhill_simplex(starting_point, himmelblau_func, iterations=iterations)
print("Downhill: Done")
h_nm_history = newton_method(starting_point, himmelblau_grad, himmelblau_hess, iterations=iterations)
print("Newton Method: Done")
h_qn_history = quasi_newton(starting_point, himmelblau_func,himmelblau_grad, iterations=iterations)
print("Quasi-Newton: Done")
# Stochastic
h_sa_history = simulated_annealing(starting_point, himmelblau_func, iterations=iterations, initial_temp=10, cooling_rate=0.999)
print("Simulated Annealing: Done")
h_pso_history = particle_swarm_optimization(himmelblau_func, num_particles=30, iterations=iterations, bounds=h_bounds)
print("Particle Swarm Optimization: Done")
h_ac_history = ant_colony_optimization(himmelblau_func, num_ants=30, iterations=200, bounds=h_bounds)
print("Ant Colony Optimization: Done")
h_ga_history = genetic_algorithm(himmelblau_func, num_individuals=num_individuals, num_generations=num_generations, bounds=h_bounds)
print("Genetic Algorithm: Done")


## Calculate Euclidean distances
print("Calculating Euclidean Distances...")
h_gd_distances = euclidean_distance(h_gd_history, h_minimum)
print("Gradient Descent: Done")
h_dh_distances = euclidean_distance(h_dh_history, h_minimum)
print("Downhill: Done")
h_nm_distances = euclidean_distance(h_nm_history, h_minimum)
print("Newton Method: Done")
h_qn_distances = euclidean_distance(h_qn_history, h_minimum)
print("Quasi-Newton: Done")
h_sa_distances = euclidean_distance(h_sa_history, h_minimum)
print("Simulated Annealing: Done")
h_pso_distances = euclidean_distance(h_pso_history, h_minimum)
print("Particle Swarm Optimization: Done")
h_ac_distances = euclidean_distance(h_ac_history, h_minimum)
print("Ant Colony Optimization: Done")
h_ga_distances = euclidean_distance(h_ga_history[-1], h_minimum)
print("Calculating Euclidean Distance: Done")

# Plot the results
plt.figure(figsize=(12, 8))
plt.step(range(len(h_gd_distances)), h_gd_distances, where='mid', label='Gradient Descent', color='green')
plt.step(range(len(h_dh_distances)), h_dh_distances, where='mid', label='Downhill', color='blue')
plt.step(range(len(h_nm_distances)), h_nm_distances, where='mid', label='Newton Method', color='yellow')
plt.step(range(len(h_qn_distances)), h_qn_distances, where='mid', label='Quasi-Newton Method', color='purple')
plt.step(range(len(h_sa_distances)), h_sa_distances, where='mid', label='Simulated Annealing', color='red')
plt.step(range(len(h_pso_distances)), h_pso_distances, where='mid', label='Particle Swarm Optimization', color='cyan')
plt.step(range(len(h_ac_distances)), h_ac_distances, where='mid', label='Ant Colony Optimization', color = 'maroon')
plt.step(range(len(h_ga_distances)), h_ga_distances, where='mid', label='Genetic Algorithm', color='magenta')
plt.xlabel('Iterations')
plt.ylabel('Euclidean Distance')
plt.title('Himmelblau Function Optimization')
plt.legend()
plt.grid(True)
plt.show()