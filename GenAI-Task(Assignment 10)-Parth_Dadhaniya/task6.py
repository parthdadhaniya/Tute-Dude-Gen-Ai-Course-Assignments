# Task 6: Filtering & Conditional Selection
import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

# 1. marks > 75
print("Students with marks > 75:")
print(df[df['Marks'] > 75])

# 2. subject is Math
print("\nStudents in Math:")
print(df[df['Subject'] == 'Math'])

# 3. marks > average
avg = df['Marks'].mean()
print("\nStudents scoring above average:")
print(df[df['Marks'] > avg])

# 4. failed students (marks < 70)
print("\nFailed students:")
print(df[df['Marks'] < 70])
