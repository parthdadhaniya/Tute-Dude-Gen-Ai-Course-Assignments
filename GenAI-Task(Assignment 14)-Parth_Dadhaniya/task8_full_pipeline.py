import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression

df = pd.read_csv("employee_data.csv")

X = df[["age", "experience", "projects_completed", "department"]]
y = df["salary"]

num_cols = ["age", "experience", "projects_completed"]
cat_cols = ["department"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(drop="first"), cat_cols)
])

# complete pipeline
pipeline = Pipeline([
    ("prep", preprocessor),
    ("model", LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)
preds = pipeline.predict(X_test)

print("Actual:   ", y_test.values[:3])
print("Predicted:", preds[:3].round(2))
print("Score:    ", round(pipeline.score(X_test, y_test), 3))
