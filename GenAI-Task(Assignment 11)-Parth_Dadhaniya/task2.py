# Task 2: Scatter Plot
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("sales_data.csv")

plt.scatter(data["Advertising_Budget"], data["Sales"])
plt.title("Advertising vs Sales")
plt.xlabel("Advertising Budget")
plt.ylabel("Sales")
plt.show()
