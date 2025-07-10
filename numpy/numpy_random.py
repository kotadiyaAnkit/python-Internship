import numpy as np

# Step 1: Create an array of 20 random integers between 1 and 100
random_array = np.random.randint(1, 101, size=20) 
#picks integers starting at 1, up to but not including 101 (so yes, 100 is included), 

print("Random Array:\n", random_array)

# Step 2: Find statistics
min_val = np.min(random_array)
max_val = np.max(random_array)
mean_val = np.mean(random_array)
std_dev = np.std(random_array)

# Print results
print("\nMinimum Value:", min_val)
print("Maximum Value:", max_val)
print("Mean:", mean_val)
print("Standard Deviation:", std_dev)
