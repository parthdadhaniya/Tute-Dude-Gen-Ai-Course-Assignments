# Task 5: Important DataFrame Functions
import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

# using dataframe functions
print("--- Info ---")
df.info()

print("\n--- Describe ---")
print(df.describe())

print("\n--- Head ---")
print(df.head())

print("\n--- Tail ---")
print(df.tail())

# sort by marks descending and reset index
sorted_df = df.sort_values(by='Marks', ascending=False)
sorted_df = sorted_df.reset_index(drop=True)

print("\nSorted by Marks (descending):")
print(sorted_df)
