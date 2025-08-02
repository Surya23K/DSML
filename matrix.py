import numpy as np

# Define matrices
A = np.array([[10, 7], [6, 4]])
B = np.array([[1, 2], [3, 5]])

add_result = A + B
sub_result = A - B
mul_result = A * B
div_result = A / B
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("\nMatrix Addition (A + B):\n", add_result)
print("\nMatrix Subtraction (A - B):\n", sub_result)
print("\nMatrix Multiplication (A * B):\n", mul_result)
print("\nMatrix Division (A / B):\n", div_result)