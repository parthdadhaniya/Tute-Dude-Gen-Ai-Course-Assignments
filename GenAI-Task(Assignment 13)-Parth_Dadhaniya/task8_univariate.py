import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("kaggle_dataset.csv").drop_duplicates()
df.columns = df.columns.str.lower().str.replace(" ", "_")
df["experience"] = df["experience"].fillna(df["experience"].median()).astype(int)
df["department"] = df["department"].fillna(df["department"].mode()[0])

# distribution of numerical column
sns.histplot(df["salary"], kde=True)
plt.show()

# count plot
sns.countplot(data=df, x="department")
plt.show()

# boxplot for outliers
sns.boxplot(y=df["salary"])
plt.show()
