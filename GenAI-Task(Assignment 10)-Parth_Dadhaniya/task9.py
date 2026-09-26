# Task 9: Mini Use Case: Sales Data Analysis
import pandas as pd
import matplotlib.pyplot as plt

sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

df = pd.DataFrame(sales)
print("Sales Data:")
print(df)

# 1. total revenue
print("\nTotal revenue:", df['Revenue'].sum())

# 2. average daily revenue
avg_rev = df['Revenue'].mean()
print("Average daily revenue:", avg_rev)

# 3. day with highest revenue
max_idx = df['Revenue'].idxmax()
print("Day with highest revenue:", df.loc[max_idx, 'Day'])

# 4. days where revenue > average
print("\nDays with revenue > average:")
print(df[df['Revenue'] > avg_rev])

# 5. plot revenue vs day
df.plot(x='Day', y='Revenue', kind='bar')
plt.show()
