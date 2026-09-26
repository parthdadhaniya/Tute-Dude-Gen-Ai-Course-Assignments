# Task 2: Mathematical Operations on Series
import pandas as pd

marks = [78, 85, 90, 66, 72]
s = pd.Series(marks)

print("Original marks:")
print(s)

# adding 5 grace marks
print("\nAdd 5 grace marks:")
print(s + 5)

# subtracting 2 marks
print("\nSubtract 2 marks:")
print(s - 2)

# multiplying by 1.05
print("\nMultiply by 1.05:")
print(s * 1.05)

# dividing by 2
print("\nDivide by 2:")
print(s / 2)
