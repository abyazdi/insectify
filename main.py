import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 500)  # X-axis: 0 to 2*pi
y = np.sin(x)  # Y-axis: sine of x

# Create the plot
plt.figure(figsize=(8, 4))  # Set the figure size
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='--')

# Add labels and title
plt.xlabel('X-axis (radians)')
plt.ylabel('Y-axis')
plt.title('Plot of Sine Wave')

# Add grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
