# Task 3: Train vs Validation vs Test Split & Tuning
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# load data
df = pd.read_csv("heart_disease.csv")

X = df[["age", "trestbps", "chol", "thalach", "oldpeak"]]
y = df["target"]

# 1. split into 60% train, 20% validation, 20% test
# first separate 20% test data
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# then split remaining 80% into 60% train and 20% val (25% of 80% is 20%)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

print("Split sizes:")
print("Train set:     ", len(X_train))
print("Validation set:", len(X_val))
print("Test set:      ", len(X_test))

# 2. tune max_depth on validation set
best_depth = 1
best_val_acc = 0.0

print("\nTuning max_depth on validation set:")
for depth in [1, 2, 3, 4, 5]:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    val_acc = dt.score(X_val, y_val)
    print("max_depth =", depth, "-> Validation Acc:", round(val_acc, 2))
    
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_depth = depth

print("\nBest max_depth:", best_depth)

# 3. evaluate final model on test set
final_model = DecisionTreeClassifier(max_depth=best_depth, random_state=42)
final_model.fit(X_train, y_train)
test_acc = final_model.score(X_test, y_test)
print("Final Model Test Accuracy:", round(test_acc, 2))
