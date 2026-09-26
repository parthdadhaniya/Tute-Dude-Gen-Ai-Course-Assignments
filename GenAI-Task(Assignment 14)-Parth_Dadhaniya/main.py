# Assignment 14: Feature Engineering, Encoding, Scaling & Pipelines
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler

df = pd.read_csv("employee_data.csv")

# Task 1: New Features
df["projects_per_year"] = df["projects_completed"] / df["experience"]
df["age_group"] = pd.cut(df["age"], bins=[20, 30, 40, 50], labels=["Young", "Mid", "Senior"])
print("Task 1 - New Features:\n", df[["age_group", "projects_per_year"]].head())

# Task 2: Date Features
df["joining_date"] = pd.to_datetime(df["joining_date"])
df["year"] = df["joining_date"].dt.year
df["month"] = df["joining_date"].dt.month
df["day"] = df["joining_date"].dt.day
print("\nTask 2 - Date Features:\n", df[["year", "month", "day"]].head())

# Task 3: One-Hot Encoding
df_dummies = pd.get_dummies(df, columns=["department"], drop_first=True)
print("\nTask 3 - Dummies:\n", df_dummies.head(2))

# Task 4: ColumnTransformer
num_cols = ["age", "experience", "projects_completed"]
cat_cols = ["department"]

ct = ColumnTransformer([
    ("ohe", OneHotEncoder(drop="first", sparse_output=False), cat_cols)
], remainder="passthrough")

data = ct.fit_transform(df[num_cols + cat_cols])
print("\nTask 4 - ColumnTransformer Shape:", data.shape)

# Task 5: StandardScaler
scaler = StandardScaler()
scaled = pd.DataFrame(scaler.fit_transform(df[num_cols]), columns=num_cols)
print("\nTask 5 - StandardScaler Mean:\n", scaled.mean().round(2))

# Task 6: MinMaxScaler
minmax = MinMaxScaler().fit_transform(df[num_cols])
print("\nTask 6 - MinMax (first row):\n", minmax[0].round(2))

# Task 7: Preprocessing Pipeline
num_pipe = Pipeline([("scale", StandardScaler())])
cat_pipe = Pipeline([("ohe", OneHotEncoder(drop="first", sparse_output=False))])

preprocessor = ColumnTransformer([
    ("num", num_pipe, num_cols),
    ("cat", cat_pipe, cat_cols)
])

# Task 8: Full Pipeline
pipeline = Pipeline([
    ("prep", preprocessor),
    ("model", LinearRegression())
])

X = df[num_cols + cat_cols]
y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

print("\nTask 8 - Actual vs Predicted:")
print("Actual:   ", y_test.values[:3])
print("Predicted:", pipeline.predict(X_test)[:3].round(2))

# Task 9: Conceptual Answers
print("\nTask 9 - Pipeline Benefits:")
print("- Bundles preprocessing and model into one.")
print("- Prevents data leakage.")
