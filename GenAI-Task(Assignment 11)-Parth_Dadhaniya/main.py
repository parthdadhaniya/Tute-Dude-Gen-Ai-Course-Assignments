# Assignment 11: Matplotlib (Core Plot Types & Visualization)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Task 1: Line Plot (Sales Trend)
data = pd.read_csv("sales_data.csv")

plt.plot(data["Month"], data["Sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# Task 2: Scatter Plot
plt.scatter(data["Advertising_Budget"], data["Sales"])
plt.title("Advertising vs Sales")
plt.xlabel("Advertising Budget")
plt.ylabel("Sales")
plt.show()


# Task 3: Bar Plot (Vertical & Horizontal)
categories = ["Electronics", "Clothing", "Home", "Books", "Toys"]
sales = [45000, 32000, 28000, 15000, 21000]

# vertical bar
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# horizontal bar
plt.barh(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Category")
plt.show()


# Task 4: Multiple Bar Plot
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


# Task 5: Stacked Bar Chart
offline = [25000, 18000, 16000, 8000, 11000]
online = [20000, 14000, 12000, 7000, 10000]

plt.bar(categories, offline, label="Offline")
plt.bar(categories, online, bottom=offline, label="Online")
plt.title("Offline vs Online Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.legend()
plt.show()


# Task 6: Histogram
marks = [45, 52, 58, 62, 65, 68, 70, 72, 74, 75, 78, 80, 82, 85, 88, 90, 92, 95]

plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()


# Task 7: Pie Chart
share = [35, 25, 20, 8, 12]

plt.pie(share, labels=categories, autopct="%1.1f%%")
plt.title("Category Share")
plt.show()
