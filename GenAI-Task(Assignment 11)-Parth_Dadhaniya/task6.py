# Task 6: Histogram
import matplotlib.pyplot as plt

marks = [45, 52, 58, 62, 65, 68, 70, 72, 74, 75, 78, 80, 82, 85, 88, 90, 92, 95]

plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()
