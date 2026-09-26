import pandas as pd

df = pd.read_csv("employee_data.csv")

# 1. projects per year of experience
df["projects_per_year"] = df["projects_completed"] / df["experience"]

# 2. age group category
df["age_group"] = pd.cut(df["age"], bins=[20, 30, 40, 50], labels=["Young", "Mid", "Senior"])

print(df[["age", "age_group", "experience", "projects_per_year"]].head())
