# Task 4: Create a DataFrame
import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

# 1. convert to dataframe
df = pd.DataFrame(students)
print("Students DataFrame:")
print(df)

# 2. print first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# 3. print last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# 4. print shape and column names
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
