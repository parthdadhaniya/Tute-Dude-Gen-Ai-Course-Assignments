import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# relplot with hue
sns.relplot(data=df, x="math_score", y="reading_score", hue="gender")
plt.show()

# same plot with scatter style
sns.relplot(data=df, x="math_score", y="reading_score", hue="gender", kind="scatter")
plt.show()
