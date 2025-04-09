import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Perform matrix operations
transposed = arr.T
sum_elements = np.sum(arr)
mean_value = np.mean(arr)
##dot = np.dot(arr, arr)
print("Original Array:\n", arr)
print("Transposed Array:\n", transposed)
print("Sum of elements:", sum_elements)
print("Mean value:", mean_value)
##print("Dot product:", dot)