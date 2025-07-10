import numpy as np

# Step 1: Create a 1D array with 12 elements
array_1d = np.arange(1, 13)
print("Original 1D Array:\n", array_1d)

# Step 2: Reshape it to a 3x4 matrix
matrix_3x4 = array_1d.reshape(3, 4)
print("\nReshaped to 3x4 Matrix:\n", matrix_3x4)

# Step 3: Flatten it back to a 1D array
flattened = matrix_3x4.flatten()
print("\nFlattened Back to 1D:\n", flattened)
