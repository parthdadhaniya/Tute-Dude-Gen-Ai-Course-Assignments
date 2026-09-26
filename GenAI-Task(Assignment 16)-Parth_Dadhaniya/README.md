# Assignment 16: SVM, Trees, Ensembles, Validation & Unsupervised Learning

This assignment covers advanced supervised algorithms, model validation strategies, and ensemble methods using scikit-learn.

## Dataset Details
- **Dataset Name:** Heart Disease Dataset (UCI / Cleveland)
- **Kaggle Link:** [Heart Disease UCI on Kaggle](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)
- **Features Used:** `age`, `trestbps`, `chol`, `thalach`, `oldpeak` (Numerical)
- **Target Variable:** `target` (Binary: 0 = No Disease, 1 = Disease)

## Files Included

- **`heart_disease.csv`**: Supervised classification dataset.
- **`task1_svm.py`**: Support Vector Machine comparing Linear and RBF kernels.
- **`task2_decision_tree.py`**: Decision tree visualization and underfitting vs overfitting comparison.
- **`task3_validation_split.py`**: 60% Train, 20% Validation, 20% Test split with hyperparameter tuning.
- **`task4_cross_validation.py`**: 5-Fold cross-validation compared against single train-test split.
- **`task5_bagging_boosting.py`**: Bagging Classifier vs AdaBoost Classifier.
- **`task6_random_forest.py`**: Random Forest evaluation, model comparison, and feature importances.
- **`main.py`**: Unified runner executing all tasks in sequence.
- **`assignment16.ipynb`**: Complete Jupyter Notebook for the assignment.

## How to Run

Run all tasks together:
```bash
python main.py
```

Or run any task individually:
```bash
python task1_svm.py
python task2_decision_tree.py
python task3_validation_split.py
python task4_cross_validation.py
python task5_bagging_boosting.py
python task6_random_forest.py
```
