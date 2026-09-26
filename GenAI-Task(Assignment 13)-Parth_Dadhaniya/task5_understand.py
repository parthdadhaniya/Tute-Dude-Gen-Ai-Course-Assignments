import pandas as pd

df = pd.read_csv("kaggle_dataset.csv")

print("Shape:", df.shape)
print("Data types:\n", df.dtypes)

num_cols = df.select_dtypes(include=["int64", "float64"]).columns
cat_cols = df.select_dtypes(include=["object"]).columns

print("Numerical columns:", list(num_cols))
print("Categorical columns:", list(cat_cols))
print("Missing values:\n", df.isnull().sum())
print("Unique counts:\n", df.nunique())
