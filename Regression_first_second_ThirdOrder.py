import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Step 1: Generate random data
np.random.seed(0)  # For reproducibility
x = np.linspace(0, 10, 50)  # 50 points between 0 and 10
y = 2 * x**3 - 5 * x**2 + 3 * x + 10 + np.random.normal(0, 100, len(x))  # Random cubic data with noise

# Step 2: Perform polynomial regression for different orders
coeffs_1 = np.polyfit(x, y, 1)  # 1st order (linear)
coeffs_2 = np.polyfit(x, y, 2)  # 2nd order (quadratic)
coeffs_3 = np.polyfit(x, y, 3)  # 3rd order (cubic)

# Polynomial functions
p1 = np.poly1d(coeffs_1)
p2 = np.poly1d(coeffs_2)
p3 = np.poly1d(coeffs_3)

# Step 3: Create subplots for each regression order
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Plot the original data and first-order regression
axs[0].scatter(x, y, color='blue', label='Data Points')
axs[0].plot(x, p1(x), color='red', label='1st Order Regression (Linear)')
axs[0].set_title('First Order Regression')
axs[0].legend()
axs[0].grid(True)

# Plot the original data and second-order regression
axs[1].scatter(x, y, color='blue', label='Data Points')
axs[1].plot(x, p2(x), color='green', label='2nd Order Regression (Quadratic)')
axs[1].set_title('Second Order Regression')
axs[1].legend()
axs[1].grid(True)

# Plot the original data and third-order regression
axs[2].scatter(x, y, color='blue', label='Data Points')
axs[2].plot(x, p3(x), color='orange', label='3rd Order Regression (Cubic)')
axs[2].set_title('Third Order Regression')
axs[2].legend()
axs[2].grid(True)

# Final plot adjustments
plt.tight_layout()
plt.show()
