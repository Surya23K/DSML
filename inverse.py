import numpy as np

A = np.array([[4, 7],
              [2, 6]])

try:
    inv_A = np.linalg.inv(A)
    print("Inverse of Matrix A:\n", inv_A)
except np.linalg.LinAlgError:
    print("Matrix A is not invertible.")
