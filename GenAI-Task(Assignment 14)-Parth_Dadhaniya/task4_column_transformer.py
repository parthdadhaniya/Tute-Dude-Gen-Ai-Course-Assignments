import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("employee_data.csv")

num_cols = ["age", "experience", "projects_completed"]
cat_cols = ["department"]

# ColumnTransformer to encode department and keep numbers
ct = ColumnTransformer([
    ("ohe", OneHotEncoder(drop="first", sparse_output=False), cat_cols)
], remainder="passthrough")

data = ct.fit_transform(df[num_cols + cat_cols])
print("Transformed shape:", data.shape)
print(data[:3])
