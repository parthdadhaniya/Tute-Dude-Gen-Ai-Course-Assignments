# Task 4: Multiple Bar Plot
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2023 = [12000, 15000, 13000, 17000, 16000, 19000]
sales_2024 = [14000, 16500, 15000, 19500, 18000, 22000]

x = np.arange(len(months))
width = 0.35

plt.bar(x - width/2, sales_2023, width, label="2023")
plt.bar(x + width/2, sales_2024, width, label="2024")

plt.xticks(x, months)
plt.title("Sales Comparison: 2023 vs 2024")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()
