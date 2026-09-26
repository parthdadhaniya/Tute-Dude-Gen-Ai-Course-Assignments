# Assignment 10: Pandas (Series, DataFrame, Functions, Filtering & Analysis)
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Pandas Series Basics
print("--- Task 1: Series Basics ---")
marks = [78, 85, 90, 66, 72]
s = pd.Series(marks)

print("Series:\n", s)
print("\nValues:", s.values)
print("Index:", s.index)
print("Data type:", s.dtype)
print("First element:", s[0])
print("\nLast two elements:\n", s.tail(2))


# Task 2: Mathematical Operations on Series
print("\n--- Task 2: Mathematical Operations ---")
print("Add 5 grace marks:\n", s + 5)
print("\nSubtract 2 marks:\n", s - 2)
print("\nMultiply by 1.05:\n", s * 1.05)
print("\nDivide by 2:\n", s / 2)


# Task 3: Python Functionalities on Series
print("\n--- Task 3: Python Functionalities ---")
print("Maximum marks:", s.max())
print("Minimum marks:", s.min())
print("Sum of marks:", s.sum())
print("Mean marks:", s.mean())

passed = s.apply(lambda x: x >= 70)
print("\nPass status (>= 70):\n", passed)
print("Number of students passed:", passed.sum())


# Task 4: Create a DataFrame
print("\n--- Task 4: Create DataFrame ---")
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

print("First 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())


# Task 5: Important DataFrame Functions
print("\n--- Task 5: DataFrame Functions ---")
df.info()
print("\nDescribe:\n", df.describe())
print("\nHead:\n", df.head())
print("\nTail:\n", df.tail())

sorted_df = df.sort_values(by='Marks', ascending=False).reset_index(drop=True)
print("\nSorted by Marks descending:\n", sorted_df)


# Task 6: Filtering & Conditional Selection
print("\n--- Task 6: Filtering ---")
print("Marks > 75:\n", df[df['Marks'] > 75])
print("\nMath subject:\n", df[df['Subject'] == 'Math'])
print("\nMarks > Average:\n", df[df['Marks'] > df['Marks'].mean()])
print("\nFailed students (Marks < 70):\n", df[df['Marks'] < 70])


# Task 7: Grouping & Basic Analysis
print("\n--- Task 7: Grouping ---")
print("Average marks per subject:\n", df.groupby('Subject')['Marks'].mean())
print("\nStudents count per subject:\n", df.groupby('Subject')['Name'].count())
print("\nMaximum marks per subject:\n", df.groupby('Subject')['Marks'].max())


# Task 8: Pandas Plotting (Simple Graphs)
print("\n--- Task 8: Plotting ---")
df.plot(x='Name', y='Marks', kind='bar')
df['Marks'].plot(kind='line')
df['Marks'].plot(kind='hist')
# plt.show()  # uncomment to display plots interactively


# Task 9: Mini Use Case: Sales Data Analysis
print("\n--- Task 9: Sales Analysis ---")
sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}
sales_df = pd.DataFrame(sales)

avg_rev = sales_df['Revenue'].mean()
print("Total revenue:", sales_df['Revenue'].sum())
print("Average daily revenue:", avg_rev)
print("Highest revenue day:", sales_df.loc[sales_df['Revenue'].idxmax(), 'Day'])
print("\nDays with revenue > average:\n", sales_df[sales_df['Revenue'] > avg_rev])

sales_df.plot(x='Day', y='Revenue', kind='bar')
# plt.show()  # uncomment to display plot interactively
