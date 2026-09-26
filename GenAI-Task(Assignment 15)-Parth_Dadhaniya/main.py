# Assignment 15: Core Algorithms, Metrics & Model Behavior
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, classification_report, confusion_matrix

df = pd.read_csv("employee_data.csv")
X = df[["age", "experience", "projects_completed"]]
y_reg = df["salary"]
y_clf = df["high_performance"]

# Task 1: Linear Regression
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y_reg, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(X_train_r, y_train_r)
preds_r = lr.predict(X_test_r)

print("Task 1 - Predictions:\n", preds_r[:3].round(2))

# Task 2: Regression Metrics
mae = mean_absolute_error(y_test_r, preds_r)
mse = mean_squared_error(y_test_r, preds_r)
rmse = np.sqrt(mse)
print("\nTask 2 - Metrics:")
print("MAE:", round(mae, 2), "| MSE:", round(mse, 2), "| RMSE:", round(rmse, 2))

# Task 3: Logistic Regression
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y_clf, test_size=0.2, random_state=42)
clf = LogisticRegression()
clf.fit(X_train_c, y_train_c)
print("\nTask 3 - Logistic Regression Accuracy:", clf.score(X_test_c, y_test_c))

# Task 4: Naive Bayes
nb = GaussianNB()
nb.fit(X_train_c, y_train_c)
print("Task 4 - Naive Bayes Accuracy:       ", nb.score(X_test_c, y_test_c))

# Task 5: KNN
print("\nTask 5 - KNN:")
for k in [1, 3, 5, 7]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_c, y_train_c)
    print(f"k = {k}, Acc: {knn.score(X_test_c, y_test_c):.2f}")

# Task 6: Classification Metrics
print("\nTask 6 - Report (Logistic Regression):")
print(classification_report(y_test_c, clf.predict(X_test_c), zero_division=0))

# Task 7: Overfitting & Underfitting
underfit = DecisionTreeClassifier(max_depth=1).fit(X_train_c, y_train_c)
overfit = DecisionTreeClassifier(max_depth=None).fit(X_train_c, y_train_c)
print("Task 7 - Underfit Train/Test:", underfit.score(X_train_c, y_train_c).round(2), "/", underfit.score(X_test_c, y_test_c).round(2))
print("Task 7 - Overfit Train/Test: ", overfit.score(X_train_c, y_train_c).round(2), "/", overfit.score(X_test_c, y_test_c).round(2))

# Task 8: Conceptual Answers
print("\nTask 8 - Concepts:")
print("Bias is error from simplicity. Variance is error from noise.")
