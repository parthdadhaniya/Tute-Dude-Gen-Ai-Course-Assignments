# Task 6: Random Forest & Feature Importances
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier

# load dataset
df = pd.read_csv("heart_disease.csv")

X = df[["age", "trestbps", "chol", "thalach", "oldpeak"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. single decision tree
tree_model = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_model.fit(X_train, y_train)
tree_acc = tree_model.score(X_test, y_test)

# 2. bagging classifier
bag_model = BaggingClassifier(n_estimators=50, random_state=42)
bag_model.fit(X_train, y_train)
bag_acc = bag_model.score(X_test, y_test)

# 3. random forest
rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
rf_model.fit(X_train, y_train)
rf_acc = rf_model.score(X_test, y_test)

print("Model Accuracy Comparison:")
print("Single Decision Tree:", round(tree_acc, 2))
print("Bagging Classifier:  ", round(bag_acc, 2))
print("Random Forest:       ", round(rf_acc, 2))

print("\nRandom Forest Feature Importances:")
for feature, imp in zip(X.columns, rf_model.feature_importances_):
    print(feature, ":", round(imp, 4))
