import pandas as pd

df = pd.read_csv("kaggle_dataset.csv").drop_duplicates()
df.columns = df.columns.str.lower().str.replace(" ", "_")
df["experience"] = df["experience"].fillna(df["experience"].median()).astype(int)
df["department"] = df["department"].fillna(df["department"].mode()[0])

# one-hot encoding
df = pd.get_dummies(df, columns=["department", "performance_rating", "city"], drop_first=True)

# separate features and target
X = df.drop(columns=["emp_id", "salary"])
y = df["salary"]

print("Features X shape:", X.shape)
print("Target y shape:", y.shape)
print(X.head())
