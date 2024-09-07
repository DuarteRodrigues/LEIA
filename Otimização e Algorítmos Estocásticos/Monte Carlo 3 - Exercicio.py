import scipy.integrate as integrate
import numpy as np

# Define the integrand function in polar coordinates
def integrand_polar(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return (x**2 + y**2) / (2 * np.pi) * r

# Perform double integration in polar coordinates
dblquad_estimate, _ = integrate.dblquad(integrand_polar, 0, 2 * np.pi, lambda theta: 0, lambda theta: 1)

print(f"SciPy dblquad Estimate: {dblquad_estimate}")