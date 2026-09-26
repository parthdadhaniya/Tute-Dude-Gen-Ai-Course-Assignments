import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# regression plot
sns.regplot(data=df, x="math_score", y="reading_score")
plt.show()

# lmplot with hue
sns.lmplot(data=df, x="math_score", y="reading_score", hue="gender")
plt.show()
