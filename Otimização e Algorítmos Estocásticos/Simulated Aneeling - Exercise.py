import numpy as np

# Define the function f(x,y)
def f(x,y):
    return (x**2 + y**2) * np.sin(1/(x**2 + y**2))

# Define the simulated aneealing algorithm
def simulated_annealing(initial_temp, cooling_rate, iterations):
    # Initial guess for x and y
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    current_value = f (x, y)
    best_x, best_y = x, y
    best_value = current_value
    temp = initial_temp

    for _ in range(iterations):
        # Generate a new candidate solution
        new_x = x + np.random.uniform(-0.1, 0.1)
        new_y = y + np.random.uniform(-0.1, 0.1)
        new_value = f(new_x, new_y)

        # Calculate the acceptance probability
        if new_value < current_value:
            acceptance_prob = 1.0
        else:
            acceptance_prob = np.exp((current_value - new_value) / temp)

        # Accept or reject the new solution
        if acceptance_prob > np.random.rand():
            x, y = new_x, new_y
            current_value = new_value

        # Update the best solution found
        if current_value < best_value:
            best_x, best_y = x, y
            best_value = current_value

        # Cool down the temperature
        temp *= cooling_rate

    return best_x, best_y, best_value

# Example usage
initial_temp = 10
cooling_rate = 0.99
iterations = 10000
best_x, best_y, best_value = simulated_annealing(initial_temp, cooling_rate, iterations)
print("Minimum x:", best_x)
print("Minimum y:", best_y)
print("Minimum value of f(x, y):", best_value)
