import numpy as np

# Step 1: Create a 4x4 array with values from 1 to 16
matrix = np.arange(1, 17).reshape(4, 4)
print("Original 4x4 Matrix:\n", matrix)

# Step 2: Extract the first two rows
first_two_rows = matrix[:1, :]  #:2 rows 0 and 1  : meaing to colums
print("\nFirst Two Rows:\n", first_two_rows)

# Step 3: Extract the last two columns
last_two_columns = matrix[:, -2:]
print("\nLast Two Columns:\n", last_two_columns)
