import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Generate random data for 180 days
np.random.seed(42)  # For reproducibility
days = np.arange(1, 181).reshape(-1, 1)  # Days from 1 to 180
values = 50 + 0.5 * days.flatten() + np.random.normal(0, 10, days.shape[0])  # Trend with noise

# Step 2: Train-test split (we'll use 80% of the data for training and 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(days, values, test_size=0.2, shuffle=False)

# Step 3: Train the model using Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict the next 30 days (day 181 to day 210)
future_days = np.arange(181, 211).reshape(-1, 1)
future_predictions = model.predict(future_days)

# Step 5: Plot the results
plt.figure(figsize=(10, 6))

# Plot the original data
plt.plot(days, values, label='Original Data (180 days)', color='blue')

# Plot the predicted values for the future days
plt.plot(future_days, future_predictions, label='Predicted Data (Next 30 days)', color='red', linestyle='--')

# Highlight the training and test sets
plt.scatter(X_train, y_train, label='Training Data', color='green')
plt.scatter(X_test, y_test, label='Test Data', color='orange')

plt.title('Linear Regression: Predicting the Next 30 Days')
plt.xlabel('Days')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
