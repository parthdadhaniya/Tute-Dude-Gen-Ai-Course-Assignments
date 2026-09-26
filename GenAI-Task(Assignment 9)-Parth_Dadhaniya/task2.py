# Task 2 - Important Mathematical Operations

import numpy as np

A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("Array A:", A)
print("Array B:", B)

# basic mathematical operations
print("\nAddition (A + B):", A + B)
print("Subtraction (A - B):", A - B)
print("Multiplication (A * B):", A * B)
print("Division (A / B):", A / B)
print("Power (A ** 2):", A ** 2)

# extra: using numpy functions
print("\nUsing NumPy functions:")
print("Addition using np.add():", np.add(A, B))
print("Subtraction using np.subtract():", np.subtract(A, B))
