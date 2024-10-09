import numpy as np
import matplotlib.pyplot as plt

# Create a random matrix for pressure (size: 150 positions, 50 time points, 100 pressure points)
np.random.seed(42)  # Seed for reproducibility
pressure_matrix = np.random.rand(150, 50, 100)

# Define the position and time points
position_point = 110
time_point = 7

# 1. Profile plot of pressure vs. time at position point 110
# Extract the pressure-time profile at position 110
pressure_time_profile = pressure_matrix[position_point, :, :].mean(axis=1)  # Averaging over pressure points

# 2. Trend plot of pressure vs. position at time point 7
# Extract the pressure-position trend at time 7
pressure_position_trend = pressure_matrix[:, time_point, :].mean(axis=1)  # Averaging over pressure points

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

# Plot 1: Pressure-Time profile at position 110
axes[0].plot(np.arange(50), pressure_time_profile, '-o')
axes[0].set_title(f'Pressure-Time Profile at Position {position_point}')
axes[0].set_xlabel('Time Points')
axes[0].set_ylabel('Average Pressure')
axes[0].grid(True)

# Plot 2: Pressure-Position trend at time 7
axes[1].plot(np.arange(150), pressure_position_trend, '-o')
axes[1].set_title(f'Pressure-Position Trend at Time {time_point}')
axes[1].set_xlabel('Position Points')
axes[1].set_ylabel('Average Pressure')
axes[1].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
