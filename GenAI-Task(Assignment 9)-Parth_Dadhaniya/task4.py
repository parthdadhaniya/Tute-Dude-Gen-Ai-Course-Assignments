# Task 4 - Aggregation Operations

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("2D Data Array:")
print(data)

# axis=1 for row-wise, axis=0 for column-wise
print("\nRow-wise sum:", np.sum(data, axis=1))
print("Column-wise sum:", np.sum(data, axis=0))
print("Minimum value:", np.min(data))
print("Maximum value:", np.max(data))
print("Overall mean:", np.mean(data))
