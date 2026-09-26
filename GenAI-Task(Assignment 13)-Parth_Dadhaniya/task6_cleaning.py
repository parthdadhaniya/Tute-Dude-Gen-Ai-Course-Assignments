import pandas as pd

df = pd.read_csv("kaggle_dataset.csv")

# 1. remove duplicates
df = df.drop_duplicates()

# 2. lowercase and snake_case column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 3. fill missing values
df["experience"] = df["experience"].fillna(df["experience"].median()).astype(int)
df["department"] = df["department"].fillna(df["department"].mode()[0])

print("Missing values after cleaning:\n", df.isnull().sum())
print(df.head())
