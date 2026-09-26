# Task 5: Bagging vs Boosting (Ensemble Learning)
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier

# load dataset
df = pd.read_csv("heart_disease.csv")

X = df[["age", "trestbps", "chol", "thalach", "oldpeak"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Concept:
# - Bagging: builds models in parallel on random data subsets to reduce variance.
# - Boosting: builds models one after another to fix mistakes from previous models to reduce bias.

# 1. Bagging Classifier
bag_model = BaggingClassifier(n_estimators=50, random_state=42)
bag_model.fit(X_train, y_train)
bag_acc = bag_model.score(X_test, y_test)

# 2. AdaBoost Classifier
boost_model = AdaBoostClassifier(n_estimators=50, random_state=42)
boost_model.fit(X_train, y_train)
boost_acc = boost_model.score(X_test, y_test)

print("Bagging Classifier Accuracy: ", round(bag_acc, 2))
print("AdaBoost Classifier Accuracy:", round(boost_acc, 2))
