import matplotlib.pyplot as plt
import numpy as np

# Create an array of angles from 0 to 2*pi (360 degrees)
theta = np.linspace(0, -3*np.pi/2, 100)

# Calculate the x and y coordinates of the points on the circle
x = np.cos(theta)
y = np.sin(theta)

# Create the plot
plt.figure(figsize=(6, 6)) # Setting the size of the figure
plt.plot(x, y)

plt.plot([1,0], [0,1], color = '#1f77b4',linestyle='-', linewidth = 2)

# Set equal aspect ratio to ensure the circle looks like a circle, not an ellipse
plt.axis('equal')

# Set the limits of the plot
plt.xlim(-1.05, 1.05)
plt.ylim(-1.05, 1.05)

# Add title and labels
plt.title("Circle with Radius 1")
plt.xlabel("X")
plt.ylabel("Y")

# Show the plot
plt.grid(True)
plt.show()