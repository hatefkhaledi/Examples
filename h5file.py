import numpy as np
import h5py
import matplotlib.pyplot as plt

# Step 1: Generate random data
np.random.seed(42)  # For reproducibility
data1 = np.random.random((100, 100))  # Random data (100x100 matrix)
data2 = np.random.random((50, 200))   # Another random dataset (50x200 matrix)

# Step 2: Create an HDF5 file and store the random datasets
file_path = '/mnt/data/random_data.h5'  # Save the file in the working directory
with h5py.File(file_path, 'w') as h5f:
    # Save the datasets in the file
    h5f.create_dataset('dataset1', data=data1)
    h5f.create_dataset('dataset2', data=data2)

# Step 3: Contour plot for both datasets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plotting the contour for dataset1
ax1.contourf(data1, cmap='jet')
ax1.set_title('Contour plot of dataset1 (100x100)')
ax1.set_aspect('equal')  # Ensure aspect ratio is equal (1:1)



# Plotting the contour for dataset2
ax2.contourf(data2, cmap='plasma')
ax2.set_title('Contour plot of dataset2 (50x200)')
ax2.set_aspect(50/200)  # Set the aspect ratio to match the dataset's shape


# Adjust the layout and show the plots
plt.tight_layout()
plt.show()

file_path
