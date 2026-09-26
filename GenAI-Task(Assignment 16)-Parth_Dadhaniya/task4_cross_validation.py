# Task 4: K-Fold Cross Validation
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier

# load data
df = pd.read_csv("heart_disease.csv")

X = df[["age", "trestbps", "chol", "thalach", "oldpeak"]]
y = df["target"]

model = DecisionTreeClassifier(max_depth=3, random_state=42)

# 1. single train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
single_acc = model.score(X_test, y_test)

# 2. 5-fold cross validation
scores = cross_val_score(model, X, y, cv=5)
mean_acc = scores.mean()

print("5-Fold Cross-Validation Scores:")
for i, score in enumerate(scores, 1):
    print("Fold", i, ":", round(score, 2))

print("\nAverage Cross-Validation Accuracy:", round(mean_acc, 2))
print("Single Train-Test Accuracy:      ", round(single_acc, 2))
