import numpy as np

# define the function to be optimized
def objective_function(x, y):
    return x**4 - 16*x**2 + 5*x + y**4 - 16*y**2 + 5*y

# define the PSO algorithm
def pso(objective_function, bounds, num_particles, max_iter):
    # initialize the swarm
    swarm_position = np.random.uniform(bounds[:, 0], bounds[:, 1], (num_particles, len(bounds)))
    swarm_velocity = np.random.uniform(-1, 1, (num_particles, len(bounds)))
    personal_best_position = swarm_position.copy()
    personal_best_value = np.array([objective_function(x,y) for x, y in personal_best_position])
    global_best_index = np.argmin(personal_best_value)
    global_best_position = personal_best_position[global_best_index]
    global_best_value = personal_best_value[global_best_index]

    # PSO iterations
    for _ in range(max_iter):
        # update particle velocity
        inertia_weight = 0.7
        cognitive_coefficient = 1.5
        social_coefficient = 2.0
        r1 = np.random.uniform(0, 1, (num_particles, len(bounds)))
        r2 = np.random.uniform(0, 1, (num_particles, len(bounds)))
        swarm_velocity = (inertia_weight * swarm_velocity) + \
                         (cognitive_coefficient * r1 * (personal_best_position - swarm_position)) + \
                         (social_coefficient * r2 * (global_best_position - swarm_position)) 
        
        # update the particle position
        swarm_position += swarm_velocity

        # bound particle position within the search space
        swarm_position = np.clip(swarm_position, bounds[:, 0], bounds[:, 1])

        # update personal best and global best
        current_value = np.array([objective_function(x, y) for x, y in swarm_position])
        personal_best_mask  = current_value < personal_best_value
        personal_best_position[personal_best_mask] = swarm_position[personal_best_mask]
        personal_best_value[personal_best_mask] = current_value[personal_best_mask]

        if np.min(personal_best_value) < global_best_value:
            global_best_index = np.argmin(personal_best_value)
            global_best_position = personal_best_position[global_best_index]
            global_best_value = personal_best_value[global_best_index]

    return global_best_position, global_best_value

# define the search space bounds
bounds = np.array([[-8, 8],[-8, 8]])    

# set PSO parameters
num_particles = 30
max_iter = 100

# run PSO
best_position, best_value = pso(objective_function, bounds, num_particles, max_iter)
print("Optimal solution found at: ", best_position)
print("Objective function value at optimal solution: ", best_value)