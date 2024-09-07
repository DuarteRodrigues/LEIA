# if you have a composed function where there is a multiplication between a number
# and the integral defined by an elipsis of a value, you use this
import numpy as np

# Define the integrand function
def integrand(x, y):
    return (x**2 + y**2) / (2 * np.pi)

# Number of random points
N = 1000000

# Generate random points in the integration domain [-1, 1] x [-1, 1]
x_random = np.random.uniform(-1, 1, N)
y_random = np.random.uniform(-1, 1, N)

# Evaluate the integrand at points within the unit circle
inside_circle = x_random**2 + y_random**2 <= 1
integrand_values = integrand(x_random[inside_circle], y_random[inside_circle])

# Estimate the integral as the average value of the integrand within the circle
# multiplied by the area of the circle (pi)
circle_area = np.pi
monte_carlo_estimate = circle_area * np.mean(integrand_values)

print(f"Monte Carlo Estimate: {monte_carlo_estimate}")
