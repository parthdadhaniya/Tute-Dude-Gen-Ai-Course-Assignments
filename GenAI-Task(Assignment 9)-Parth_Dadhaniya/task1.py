# Task 1 - Creating NumPy Arrays

import numpy as np

# 1D array of integers from 1 to 10
arr1 = np.arange(1, 11)

# 2D array of shape (3, 3) with values from 1 to 9
arr2 = np.arange(1, 10).reshape(3, 3)

# NumPy array from list
my_list = [10, 20, 30, 40, 50]
arr3 = np.array(my_list)

print("1D Array:")
print(arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("\n2D Array (3x3):")
print(arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)

print("\nArray from list:")
print(arr3)
print("Shape:", arr3.shape)
print("Data Type:", arr3.dtype)
