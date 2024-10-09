import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter1d

# Step 1: Generate random data
np.random.seed(42)  # For reproducibility
x = np.linspace(0, 100, 200)  # Generate 200 points between 0 and 100
y = np.sin(x / 10) + np.random.normal(0, 0.5, size=x.size)  # Random sine wave with noise

# Step 2: Smooth the data using a moving average (uniform filter)
window_size = 5  # Define window size for smoothing
y_smooth = uniform_filter1d(y, size=window_size)

# Step 3: Plot the original and smoothed data
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Original Data', alpha=0.5, color='blue', linestyle='--')
plt.plot(x, y_smooth, label='Smoothed Data', color='red')
plt.title('Random Data with Smoothing')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
