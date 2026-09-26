import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# bar plot
sns.barplot(data=df, x="gender", y="math_score")
plt.show()

# box plot
sns.boxplot(data=df, x="gender", y="math_score")
plt.show()

# violin plot
sns.violinplot(data=df, x="gender", y="math_score")
plt.show()

# count plot
sns.countplot(data=df, x="gender")
plt.show()
