import numpy as np
import matplotlib.pyplot as plt

particle_num = 100
avg = 0
std_dv = 1
time_step = 0.01

# Define the time range
t = np.arange(0, 6, time_step)

# Calculate the sinusoidal function
s = np.sin(2 * np.pi * t)

for i in range(len(t)):
    x = np.linspace(-5,5, 100)

# Plot '+' symbols for every 0.05 interval
plt.scatter(t[::int(time_step/time_step)], s[::int(time_step/time_step)], marker='+', color='blue', label='Position')
  
    ##TODO: Place the gaussian curve in the first time step with the curve determined by standard deviation an position determined by average
    ##TODO: For each gaussian, generate 25 random dots behind each curve
    ##TODO: Calculate the average and standard deviation os the X and Y coordinates of the generated points
    ##TODO: Plot the average position of the points with a '+' character
    ##TODO: Gererate the next gaussian curve on the basis of the previous standard deviation and average calculations 

# Set plot labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Sinusoidal Function with Positions')

# Set y-axis limits to show two cycles of the sinus wave
plt.xlim(0, 2)

# Add legend
plt.legend()

# Show plot
plt.grid(False)
plt.show()
