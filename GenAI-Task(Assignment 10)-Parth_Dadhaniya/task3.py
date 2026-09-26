# Task 3: Python Functionalities on Series
import pandas as pd

marks = [78, 85, 90, 66, 72]
s = pd.Series(marks)

# basic stats
print("Maximum marks:", s.max())
print("Minimum marks:", s.min())
print("Sum of marks:", s.sum())
print("Mean marks:", s.mean())

# check pass or fail (>= 70) using lambda
passed = s.apply(lambda x: x >= 70)
print("\nPassed students (True/False):")
print(passed)

# count how many passed
print("\nNumber of students passed:", passed.sum())
