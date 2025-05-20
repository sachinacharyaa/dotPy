#array 
# a = [1, "Hello", [3.14, "world"]]
# print(a)

# a.append(2)  # Add an integer to the end
# print(a)




# NumPy arrays are a part of the NumPy library,
# which is a powerful tool for numerical computing in Python.
#np.array()

import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4])

# Element-wise operations
print(arr * 2)  

# Multi-dimensional array
arr2d = np.array([[1, 2], [3, 4]])
print(arr2d * 2)