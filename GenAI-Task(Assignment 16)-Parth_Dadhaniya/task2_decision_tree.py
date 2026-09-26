# Task 2: Decision Tree Classifier & Overfitting/Underfitting
# Author: Parth Dadhaniya

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv("heart_disease.csv")

X = df[["age", "trestbps", "chol", "thalach", "oldpeak"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# training a small tree with depth 2 to visualize easily
dt = DecisionTreeClassifier(max_depth=2, random_state=42)
dt.fit(X_train, y_train)

# plotting and saving tree
plt.figure(figsize=(8, 5))
plot_tree(dt, feature_names=list(X.columns), class_names=["No Disease", "Disease"], filled=True)
plt.title("Decision Tree Structure (depth=2)")
plt.savefig("decision_tree.png")
plt.close()
print("Tree plot saved as decision_tree.png")

# 1. low max_depth = underfitting (model is too simple)
underfit_model = DecisionTreeClassifier(max_depth=1, random_state=42)
underfit_model.fit(X_train, y_train)

# 2. unconstrained depth = overfitting (memorizes training set)
overfit_model = DecisionTreeClassifier(max_depth=None, random_state=42)
overfit_model.fit(X_train, y_train)

print("\nUnderfit Model (depth=1):")
print("Train Score:", round(underfit_model.score(X_train, y_train), 2))
print("Test Score: ", round(underfit_model.score(X_test, y_test), 2))

print("\nOverfit Model (unlimited depth):")
print("Train Score:", round(overfit_model.score(X_train, y_train), 2))
print("Test Score: ", round(overfit_model.score(X_test, y_test), 2))
