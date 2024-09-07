# Name: Tracking - Particle Filter Pi Ratio.py
#
# Author: Duarte Rodrigues - DuarteRodrigues @Github
# Student ID: a22206488
# Date: July 2024
# Description: This script is used to apply the Particle Filter algorithm to a space with two different shapes (Square and Circle) and calculate the ratio between the particles occupied in the square and the particles occupied in the circle
#              This will be used to prove that this ratio, even tho it relies on the use of random particle spawn points, will always approximate towards Pi

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random as rd

# Define the characteristics of the environment
environment_x = 12
environment_y = 8
side_length = 3
radius = side_length
gap = 2
particle_num = 2000

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the square
square_center_y = environment_y / 2 # Vertical center of the square
square = patches.Rectangle((1, square_center_y - side_length / 2), side_length, side_length, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(square)

# Plot the circle
circle_center_x = side_length + gap + radius
circle = patches.Circle((circle_center_x, radius+1), radius, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(circle)

# Generate random points
points_x = np.random.uniform(0, environment_x, particle_num)
points_y = np.random.uniform(0, environment_y, particle_num)

# Determine point colors and point count inside each shape
points_in_square = 0
points_in_circle = 0
colors = []
ratios = []

for x, y in zip(points_x, points_y):
    if 1 <= x <= 1 + side_length and (square_center_y - side_length / 2) <= y <= (square_center_y + side_length / 2):
        colors.append('green') # Inside the square
        points_in_square += 1
    elif(x - circle_center_x)**2 + (y - (radius + 1))**2 <= radius**2:
        colors.append('magenta') # Inside the circle
        points_in_circle += 1
    else:
        colors.append('black') # Outside both shapes

    # Calculate the ratio
    ratio = points_in_circle / points_in_square if points_in_square > 0 else np.nan
    ratios.append(ratio)

# Plot the points
ax.scatter(points_x, points_y, c=colors, s=10)

# Set the aspect of the plot to be equal
ax.set_aspect('equal', adjustable='box')

# Set the limits of the plot
ax.set_xlim(0, environment_x)
ax.set_ylim(0, environment_y)

# Display the plot for the environment
plt.show()

# Plot the ratio
fig, ax = plt.subplots()
ax.plot(range(1, particle_num+1), ratios, label='Circle/Square Ratio')

# Draw a horizontal line at y = py
ax.axhline(y=np.pi, color='r', linestyle='--', label='y = pi')

# Set labels and title
ax.set_xlabel('Total number of Points')
ax.set_ylabel('Points in Circle/Points in Square Ratio')
ax.set_title('Ratio of Points in Circle to Points in Square')
ax.legend()

# Display the ratio plot
plt.show()