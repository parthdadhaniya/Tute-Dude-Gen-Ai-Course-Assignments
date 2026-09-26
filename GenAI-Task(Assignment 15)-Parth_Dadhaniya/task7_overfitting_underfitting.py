import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("employee_data.csv")

X = df[["age", "experience", "projects_completed"]]
y = df["high_performance"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# simple model (underfitting)
underfit = DecisionTreeClassifier(max_depth=1)
underfit.fit(X_train, y_train)
print("Underfit (max_depth=1):")
print("Train:", underfit.score(X_train, y_train).round(2))
print("Test: ", underfit.score(X_test, y_test).round(2))

# complex model (overfitting)
overfit = DecisionTreeClassifier(max_depth=None)
overfit.fit(X_train, y_train)
print("\nOverfit (unlimited depth):")
print("Train:", overfit.score(X_train, y_train).round(2))
print("Test: ", overfit.score(X_test, y_test).round(2))
