# Task 7 - Mini Use Case: Sales Analysis

import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
days = np.array(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"])

print("Daily Sales:", sales)

# 1. total weekly sales
total_sales = np.sum(sales)
print("\nTotal weekly sales:", total_sales)

# 2. average daily sales
avg_sales = np.mean(sales)
print("Average daily sales:", round(avg_sales, 2))

# 3. highest and lowest sales day
max_day = days[np.argmax(sales)]
min_day = days[np.argmin(sales)]
print("Highest sales day:", max_day, "with sales of", np.max(sales))
print("Lowest sales day:", min_day, "with sales of", np.min(sales))

# 4. standard deviation of sales
std_sales = np.std(sales)
print("Standard deviation of sales:", round(std_sales, 2))

# 5. days where sales were above average
above_avg_days = days[sales > avg_sales]
above_avg_sales = sales[sales > avg_sales]
print("Days with above average sales:", above_avg_days)
print("Sales on those days:", above_avg_sales)
