# Assignment 9 - NumPy (Mathematical & Statistical Operations)

import numpy as np

# --- Task 1: Creating NumPy Arrays ---
print("--- Task 1: Creating NumPy Arrays ---")
arr1 = np.arange(1, 11)
arr2 = np.arange(1, 10).reshape(3, 3)
arr3 = np.array([10, 20, 30, 40, 50])

print("1D Array:", arr1)
print("Shape:", arr1.shape, "| Dtype:", arr1.dtype)

print("\n2D Array:\n", arr2)
print("Shape:", arr2.shape, "| Dtype:", arr2.dtype)

print("\nArray from list:", arr3)
print("Shape:", arr3.shape, "| Dtype:", arr3.dtype)


# --- Task 2: Important Mathematical Operations ---
print("\n--- Task 2: Important Mathematical Operations ---")
A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("Addition (A + B):", A + B)
print("Subtraction (A - B):", A - B)
print("Multiplication (A * B):", A * B)
print("Division (A / B):", A / B)
print("Power (A ** 2):", A ** 2)
print("Using np.add():", np.add(A, B))
print("Using np.subtract():", np.subtract(A, B))


# --- Task 3: Important NumPy Mathematical Formulas ---
print("\n--- Task 3: Important NumPy Mathematical Formulas ---")
values = np.array([2, 4, 6, 8, 10])

print("Square root:", np.sqrt(values))
print("Exponential:", np.exp(values))
print("Natural log:", np.log(values))
print("Sum:", np.sum(values))
print("Cumulative sum:", np.cumsum(values))


# --- Task 4: Aggregation Operations ---
print("\n--- Task 4: Aggregation Operations ---")
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Row-wise sum:", np.sum(data, axis=1))
print("Column-wise sum:", np.sum(data, axis=0))
print("Minimum value:", np.min(data))
print("Maximum value:", np.max(data))
print("Overall mean:", np.mean(data))


# --- Task 5: Statistical Operations ---
print("\n--- Task 5: Statistical Operations ---")
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", round(np.std(marks), 2))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Range:", np.max(marks) - np.min(marks))


# --- Task 6: Percentiles & Sorting ---
print("\n--- Task 6: Percentiles & Sorting ---")
print("Sorted marks:", np.sort(marks))
print("25th percentile:", np.percentile(marks, 25))
print("50th percentile:", np.percentile(marks, 50))
print("75th percentile:", np.percentile(marks, 75))
print("Students above average:", np.sum(marks > np.mean(marks)))


# --- Task 7: Mini Use Case: Sales Analysis ---
print("\n--- Task 7: Sales Analysis ---")
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
days = np.array(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"])

avg_sales = np.mean(sales)
print("Total weekly sales:", np.sum(sales))
print("Average daily sales:", round(avg_sales, 2))
print("Highest sales day:", days[np.argmax(sales)], f"({np.max(sales)})")
print("Lowest sales day:", days[np.argmin(sales)], f"({np.min(sales)})")
print("Standard deviation:", round(np.std(sales), 2))
print("Days above average:", days[sales > avg_sales])
