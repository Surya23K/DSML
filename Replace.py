import numpy as np

# 1D array with 24 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape into 3D array with shape (2, 2, 3)
newarr = arr.reshape(2, 2,3)

print(newarr)
print("Shape of new array:", newarr.shape)