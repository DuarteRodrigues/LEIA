import numpy as np

# Define the integrand function
def integrand(x, y):
    return (x**2 + y**2) / (2 * np.pi)

# Create grid points
num_points = 1000
x = np.linspace(-1, 1, num_points)
y = np.linspace(-1, 1, num_points)

# Create meshgrid
X, Y = np.meshgrid(x, y)
Z = integrand(X, Y)

# Mask out points outside the unit circle
mask = (X**2 + Y**2) <= 1
Z_masked = np.where(mask, Z, 0)

# Use the trapezoidal rule to estimate the integral over the unit circle
dx = dy = 2 / (num_points - 1)  # The step size in x and y directions
trapz_estimate = np.trapz(np.trapz(Z_masked, dx=dx, axis=0), dx=dy)

# Scale the estimate by the ratio of the area of the unit circle to the integration domain area
trapz_estimate *= (np.pi / 4)

print(f"Trapezoidal Rule Estimate: {trapz_estimate}")