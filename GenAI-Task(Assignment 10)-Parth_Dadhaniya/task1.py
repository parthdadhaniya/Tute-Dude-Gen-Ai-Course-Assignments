# Task 1: Pandas Series Basics
import pandas as pd

marks = [78, 85, 90, 66, 72]
s = pd.Series(marks)

# print series, values, index, and dtype
print("Series:")
print(s)
print("\nValues:", s.values)
print("Index:", s.index)
print("Data type:", s.dtype)

# access first element and last two elements
print("\nFirst element:", s[0])
print("\nLast two elements:")
print(s.tail(2))
