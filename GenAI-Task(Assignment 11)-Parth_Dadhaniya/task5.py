# Task 5: Stacked Bar Chart
import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Home", "Books", "Toys"]
offline = [25000, 18000, 16000, 8000, 11000]
online = [20000, 14000, 12000, 7000, 10000]

plt.bar(categories, offline, label="Offline")
plt.bar(categories, online, bottom=offline, label="Online")

plt.title("Offline vs Online Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.legend()
plt.show()
