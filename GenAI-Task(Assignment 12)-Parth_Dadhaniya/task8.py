import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# FacetGrid
g = sns.FacetGrid(df, col="gender")
g.map(sns.scatterplot, "math_score", "reading_score")
plt.show()

# multi-plots using relplot, catplot, and displot
sns.relplot(data=df, x="math_score", y="reading_score", hue="gender", col="lunch")
plt.show()

sns.catplot(data=df, x="gender", y="math_score", kind="box")
plt.show()

sns.displot(df["math_score"], kde=True)
plt.show()
