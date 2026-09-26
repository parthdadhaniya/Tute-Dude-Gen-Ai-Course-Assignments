# Task 1: Support Vector Machine (SVM)
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# loading the dataset
df = pd.read_csv("heart_disease.csv")

# selecting numerical features and target
X = df[["age", "trestbps", "chol", "thalach", "oldpeak"]]
y = df["target"]

# 80-20 train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scaling features because SVM distance calculations need normalized features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. linear kernel
model_linear = SVC(kernel="linear", random_state=42)
model_linear.fit(X_train_scaled, y_train)
acc_linear = model_linear.score(X_test_scaled, y_test)

# 2. rbf kernel
model_rbf = SVC(kernel="rbf", random_state=42)
model_rbf.fit(X_train_scaled, y_train)
acc_rbf = model_rbf.score(X_test_scaled, y_test)

print("Linear Kernel Accuracy:", round(acc_linear, 2))
print("RBF Kernel Accuracy:   ", round(acc_rbf, 2))
