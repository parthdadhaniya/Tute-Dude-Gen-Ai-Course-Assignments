import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.read_csv("employee_data.csv")

num_cols = ["age", "experience", "projects_completed"]
cat_cols = ["department"]

# numerical and categorical pipelines
num_pipe = Pipeline([("scaler", StandardScaler())])
cat_pipe = Pipeline([("ohe", OneHotEncoder(drop="first", sparse_output=False))])

preprocessor = ColumnTransformer([
    ("num", num_pipe, num_cols),
    ("cat", cat_pipe, cat_cols)
])

result = preprocessor.fit_transform(df[num_cols + cat_cols])
print("Processed shape:", result.shape)
print(result[:3].round(2))
