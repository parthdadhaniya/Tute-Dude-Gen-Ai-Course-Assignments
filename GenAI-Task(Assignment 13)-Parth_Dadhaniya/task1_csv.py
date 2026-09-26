import pandas as pd

df = pd.read_csv("kaggle_dataset.csv")

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
df.info()
print(df.describe())
