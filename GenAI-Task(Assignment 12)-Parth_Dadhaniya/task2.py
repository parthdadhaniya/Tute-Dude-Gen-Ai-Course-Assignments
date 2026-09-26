import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# line plot
sns.lineplot(data=df, x="math_score", y="reading_score")
plt.show()

# scatter-style line plot
sns.lineplot(data=df, x="math_score", y="reading_score", marker="o")
plt.show()

# faceted line plot by gender
sns.relplot(data=df, x="math_score", y="reading_score", kind="line", col="gender")
plt.show()
