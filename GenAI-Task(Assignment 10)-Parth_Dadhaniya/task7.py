# Task 7: Grouping & Basic Analysis
import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

# 1. average marks per subject
print("Average marks per subject:")
print(df.groupby('Subject')['Marks'].mean())

# 2. number of students per subject
print("\nCount of students per subject:")
print(df.groupby('Subject')['Name'].count())

# 3. maximum marks per subject
print("\nMaximum marks per subject:")
print(df.groupby('Subject')['Marks'].max())
