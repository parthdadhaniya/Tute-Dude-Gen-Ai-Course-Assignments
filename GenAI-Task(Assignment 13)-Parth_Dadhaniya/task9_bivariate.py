import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("kaggle_dataset.csv").drop_duplicates()
df.columns = df.columns.str.lower().str.replace(" ", "_")
df["experience"] = df["experience"].fillna(df["experience"].median()).astype(int)
df["department"] = df["department"].fillna(df["department"].mode()[0])

# scatter plot
sns.scatterplot(data=df, x="experience", y="salary", hue="department")
plt.show()

# correlation heatmap
sns.heatmap(df[["age", "experience", "salary"]].corr(), annot=True)
plt.show()

# bar plot
sns.barplot(data=df, x="department", y="salary")
plt.show()

# box plot
sns.boxplot(data=df, x="department", y="salary")
plt.show()
