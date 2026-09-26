# Task 1: Line Plot (Sales Trend)
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("sales_data.csv")

plt.plot(data["Month"], data["Sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
