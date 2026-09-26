# Task 8: Pandas Plotting (Simple Graphs)
import pandas as pd
import matplotlib.pyplot as plt

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

# 1. bar graph of student names vs marks
df.plot(x='Name', y='Marks', kind='bar')
plt.show()

# 2. line graph of marks
df['Marks'].plot(kind='line')
plt.show()

# 3. histogram of marks
df['Marks'].plot(kind='hist')
plt.show()
