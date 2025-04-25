import numpy as np

# Create the array
arr = np.array([1, 1, 0, 0, 1, 0, 0, 1, 1, 0])

# Count the number of 1s
count = np.count_nonzero(arr == 1)

print(f"Number of 1s in the array: {count}") 