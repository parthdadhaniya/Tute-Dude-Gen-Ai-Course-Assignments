import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("employee_data.csv")

X = df[["age", "experience", "projects_completed"]]
y = df["high_performance"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression()
clf.fit(X_train, y_train)

preds = clf.predict(X_test)
print("Actual:     ", y_test.values)
print("Predictions:", preds)
print("Accuracy:   ", clf.score(X_test, y_test))
