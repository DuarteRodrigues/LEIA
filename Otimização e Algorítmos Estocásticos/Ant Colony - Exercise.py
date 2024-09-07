import numpy as np
import random

# Function to calculate the cost of moving from (x1, y1) to (x2, y2)
def cost(x1, y1, x2, y2, n):
    return 0.5 - (x2 * y2) / (n ** 2)

# Function to initialize pheromone matrix
def initialize_pheromones(n):
    return np.ones((n+1, n+1))

# Function to update pheromone matrix
def update_pheromones(pheromones, path, total_cost):
    evaporation_rate = 0.5
    pheromones *= (1 - evaporation_rate)
    for i in range(len(path)-1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        pheromones[x1][y1] += 1 / total_cost
        pheromones[x2][y2] += 1 / total_cost
    return pheromones

# Function to select the next position based on pheromone levels and heuristic information
def select_next_position(pheromones, visited, x, y, n):
    alpha = 1
    beta = 2
    options = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= x + dx <= n and 0 <= y + dy <= n and (dx != 0 or dy != 0) and (x + dx, y + dy) not in visited:
                cost_val = cost(x, y, x + dx, y + dy, n)
                pheromone_val = pheromones[x + dx][y + dy]
                heuristic_val = 1 / cost_val
                probability = (pheromone_val ** alpha) * (heuristic_val ** beta)
                options.append(((x + dx, y + dy), probability))
    total_prob = sum(prob for pos, prob in options)
    options = [(pos, prob / total_prob) for pos, prob in options]
    chosen_pos = random.choices([pos for pos, prob in options], weights=[prob for pos, prob in options])[0]
    return chosen_pos

# Ant colony optimization function
def ant_colony_optimization(n, num_ants, iterations):
    pheromones = initialize_pheromones(n)
    best_path = []
    best_cost = float('inf')
    for _ in range(iterations):
        for ant in range(num_ants):
            path = [(0, 0)]
            visited = set([(0, 0)])
            total_cost = 0
            x, y = 0, 0
            while (x, y) != (n, n):
                x, y = select_next_position(pheromones, visited, x, y, n)
                path.append((x, y))
                visited.add((x, y))
                total_cost += cost(path[-2][0], path[-2][1], x, y, n)
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path
        pheromones = update_pheromones(pheromones, best_path, best_cost)
    return best_path, best_cost

# Example usage
n = 10000
num_ants = 10
iterations = 100
best_path, best_cost = ant_colony_optimization(n, num_ants, iterations)
print("Best path:", best_path)
print("Best cost:", best_cost)