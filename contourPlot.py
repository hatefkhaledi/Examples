import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points (x, y)
x = np.linspace(0, 10, 100)  # x-axis points
y = np.linspace(0, 10, 100)  # y-axis points
X, Y = np.meshgrid(x, y)

# Generate some sample pressure data (for example, a 2D Gaussian function as pressure)
pressure = np.sin(X) * np.cos(Y)  # This is just an example for pressure distribution

# Create a contour plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, pressure, cmap='viridis')

# Add color bar to show pressure scale
plt.colorbar(contour, label='Pressure')

# Add labels and title
plt.title('Contour Plot of Pressure')
plt.xlabel('X Position')
plt.ylabel('Y Position')

# Show the plot
plt.show()
