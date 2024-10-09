import pandas as pd
import matplotlib.pyplot as plt

# File path on drive D
file_path = r'D:\Python\ReadData.xlsx'  # Replace 'your_file.xlsx' with the actual file name

# Read the Excel file, by default it reads the first sheet. If you need a specific sheet, use sheet_name parameter
df = pd.read_excel(file_path)

# Assuming the first column is X and the second column is Y
x = df.iloc[:, 0]  # First column (index 0)
y = df.iloc[:, 1]  # Second column (index 1)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data from Excel')
plt.title('XY Plot of First Two Columns from Excel')
plt.xlabel('Column 1 (X)')
plt.ylabel('Column 2 (Y)')
plt.grid(True)
plt.legend()
plt.show()
