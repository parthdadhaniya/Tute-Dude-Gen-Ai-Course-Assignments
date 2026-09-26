# Task 6 - Percentiles & Sorting

import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

# sorting the array
sorted_marks = np.sort(marks)
print("Sorted marks:", sorted_marks)

# finding percentiles
print("25th percentile:", np.percentile(marks, 25))
print("50th percentile:", np.percentile(marks, 50))
print("75th percentile:", np.percentile(marks, 75))

# counting students who scored above average
avg_marks = np.mean(marks)
above_avg_count = np.sum(marks > avg_marks)

print("Average marks:", avg_marks)
print("Students scored above average:", above_avg_count)
