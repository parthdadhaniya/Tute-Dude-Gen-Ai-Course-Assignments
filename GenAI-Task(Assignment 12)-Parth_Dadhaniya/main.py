# Assignment 12: Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# Task 1: Relational Plot
sns.relplot(data=df, x="math_score", y="reading_score", hue="gender")
plt.show()

sns.relplot(data=df, x="math_score", y="reading_score", hue="gender", kind="scatter")
plt.show()

# Task 2: Line Plot as Scatter & Facet
sns.lineplot(data=df, x="math_score", y="reading_score")
plt.show()

sns.lineplot(data=df, x="math_score", y="reading_score", marker="o")
plt.show()

sns.relplot(data=df, x="math_score", y="reading_score", kind="line", col="gender")
plt.show()

# Task 3: Distribution Plots
sns.histplot(df["math_score"])
plt.show()

sns.kdeplot(df["math_score"])
plt.show()

sns.rugplot(df["math_score"])
plt.show()

sns.histplot(df["math_score"], kde=True)
plt.show()

# Task 4: Bivariate Distribution Plots
sns.histplot(data=df, x="math_score", y="reading_score")
plt.show()

sns.kdeplot(data=df, x="math_score", y="reading_score")
plt.show()

# Task 5: Matrix Plots
sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# Task 6: Categorical Plots
sns.barplot(data=df, x="gender", y="math_score")
plt.show()

sns.boxplot(data=df, x="gender", y="math_score")
plt.show()

sns.violinplot(data=df, x="gender", y="math_score")
plt.show()

sns.countplot(data=df, x="gender")
plt.show()

# Task 7: Regression Plots
sns.regplot(data=df, x="math_score", y="reading_score")
plt.show()

sns.lmplot(data=df, x="math_score", y="reading_score", hue="gender")
plt.show()

# Task 8: Multi-Plots & Figure-Level Plots
g = sns.FacetGrid(df, col="gender")
g.map(sns.scatterplot, "math_score", "reading_score")
plt.show()

sns.relplot(data=df, x="math_score", y="reading_score", hue="gender", col="lunch")
plt.show()

sns.catplot(data=df, x="gender", y="math_score", kind="box")
plt.show()

sns.displot(df["math_score"], kde=True)
plt.show()
