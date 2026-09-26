# Task 7: Pie Chart
import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Home", "Books", "Toys"]
share = [35, 25, 20, 8, 12]

plt.pie(share, labels=categories, autopct="%1.1f%%")
plt.title("Category Share")
plt.show()
