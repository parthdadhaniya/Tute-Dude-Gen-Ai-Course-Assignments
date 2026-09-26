# Task 3: Bar Plot
import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Home", "Books", "Toys"]
sales = [45000, 32000, 28000, 15000, 21000]

# vertical bar chart
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# horizontal bar chart
plt.barh(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Category")
plt.show()
