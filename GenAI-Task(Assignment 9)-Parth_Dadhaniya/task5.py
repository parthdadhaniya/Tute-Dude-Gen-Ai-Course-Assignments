# Task 5 - Statistical Operations

import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
print("Marks:", marks)

# calculating stats
mean_val = np.mean(marks)
median_val = np.median(marks)
var_val = np.var(marks)
std_val = np.std(marks)
min_val = np.min(marks)
max_val = np.max(marks)
range_val = max_val - min_val

print("\nMean:", mean_val)
print("Median:", median_val)
print("Variance:", var_val)
print("Standard Deviation:", round(std_val, 2))
print("Minimum:", min_val)
print("Maximum:", max_val)
print("Range (max - min):", range_val)
