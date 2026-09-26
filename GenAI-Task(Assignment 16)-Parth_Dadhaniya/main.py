# Assignment 16: SVM, Trees, Ensembles, Validation & Unsupervised Learning
# Author: Parth Dadhaniya

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier, RandomForestClassifier

# load Kaggle heart disease dataset
df = pd.read_csv("heart_disease.csv")
X = df[["age", "trestbps", "chol", "thalach", "oldpeak"]]
y = df["target"]

# Task 1: Support Vector Machine (SVM)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_linear = SVC(kernel="linear", random_state=42).fit(X_train_scaled, y_train)
svm_rbf = SVC(kernel="rbf", random_state=42).fit(X_train_scaled, y_train)

print("Task 1 - SVM Kernels:")
print("Linear Kernel Accuracy:", round(svm_linear.score(X_test_scaled, y_test), 2))
print("RBF Kernel Accuracy:   ", round(svm_rbf.score(X_test_scaled, y_test), 2))

# Task 2: Decision Tree Algorithm
dt = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_train, y_train)

plt.figure(figsize=(8, 5))
plot_tree(dt, feature_names=list(X.columns), class_names=["No Disease", "Disease"], filled=True)
plt.title("Decision Tree Visualization")
plt.savefig("decision_tree.png")
plt.close()

dt_under = DecisionTreeClassifier(max_depth=1, random_state=42).fit(X_train, y_train)
dt_over = DecisionTreeClassifier(max_depth=None, random_state=42).fit(X_train, y_train)

print("\nTask 2 - Decision Tree:")
print("Underfitting (depth=1)   - Train:", round(dt_under.score(X_train, y_train), 2), "| Test:", round(dt_under.score(X_test, y_test), 2))
print("Overfitting  (depth=None) - Train:", round(dt_over.score(X_train, y_train), 2), "| Test:", round(dt_over.score(X_test, y_test), 2))

# Task 3: Train vs Validation vs Test Split
X_temp, X_test3, y_temp, y_test3 = train_test_split(X, y, test_size=0.2, random_state=42)
X_tr, X_val, y_tr, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

best_depth = 1
best_val = 0.0
for d in [1, 2, 3, 4, 5]:
    m = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_tr, y_tr)
    val_acc = m.score(X_val, y_val)
    if val_acc > best_val:
        best_val = val_acc
        best_depth = d

final_dt = DecisionTreeClassifier(max_depth=best_depth, random_state=42).fit(X_tr, y_tr)

print("\nTask 3 - Train / Validation / Test Split:")
print("Tuned max_depth:          ", best_depth, "(Val Acc:", round(best_val, 2), ")")
print("Final Model Test Accuracy:", round(final_dt.score(X_test3, y_test3), 2))

# Task 4: Cross-Validation
dt_cv = DecisionTreeClassifier(max_depth=3, random_state=42)
cv_scores = cross_val_score(dt_cv, X, y, cv=5)

print("\nTask 4 - 5-Fold Cross-Validation:")
print("Fold Scores:     ", [round(s, 2) for s in cv_scores])
print("Mean CV Accuracy:", round(cv_scores.mean(), 2))

# Task 5: Ensemble Learning (Bagging vs Boosting)
bag = BaggingClassifier(n_estimators=50, random_state=42).fit(X_train, y_train)
boost = AdaBoostClassifier(n_estimators=50, random_state=42).fit(X_train, y_train)

print("\nTask 5 - Bagging vs Boosting:")
print("Bagging Accuracy: ", round(bag.score(X_test, y_test), 2))
print("AdaBoost Accuracy:", round(boost.score(X_test, y_test), 2))

# Task 6: Random Forest
rf = RandomForestClassifier(n_estimators=50, random_state=42).fit(X_train, y_train)

print("\nTask 6 - Random Forest Comparison:")
print("Single Tree:  ", round(dt.score(X_test, y_test), 2))
print("Bagging:      ", round(bag.score(X_test, y_test), 2))
print("Random Forest:", round(rf.score(X_test, y_test), 2))

print("\nFeature Importances:")
for col, imp in zip(X.columns, rf.feature_importances_):
    print(col, ":", round(imp, 4))
