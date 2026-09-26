# Assignment 10: Pandas (Series, DataFrame, Functions, Filtering & Analysis)

This folder contains my Python solutions for Assignment 10 on Pandas. It covers Pandas Series, Series math operations, Series functions with lambda expressions, DataFrame creation, basic inspection functions, conditional filtering, groupby aggregations, Pandas plotting, and a mini sales data analysis use case.

## Task Details

* **task1.py (Pandas Series Basics)**
  Creates a Series from marks list `[78, 85, 90, 66, 72]`, prints values, index, data type, and accesses first and last two elements.

* **task2.py (Mathematical Operations on Series)**
  Performs element-wise addition (+5), subtraction (-2), multiplication (*1.05), and division (/2) on the marks Series.

* **task3.py (Python Functionalities on Series)**
  Finds maximum, minimum, sum, and mean marks, applies a lambda function for pass/fail (>= 70), and counts students passed.

* **task4.py (Create a DataFrame)**
  Converts a students dictionary into a DataFrame, prints the first 3 rows, last 2 rows, shape, and column names.

* **task5.py (Important DataFrame Functions)**
  Demonstrates `.info()`, `.describe()`, `.head()`, and `.tail()`, sorts students by Marks descending, and resets index.

* **task6.py (Filtering & Conditional Selection)**
  Filters students scoring > 75, students in Math, students scoring > average marks, and students who failed (< 70).

* **task7.py (Grouping & Basic Analysis)**
  Calculates average marks per subject, student counts per subject, and maximum marks per subject using `.groupby()`.

* **task8.py (Pandas Plotting)**
  Plots a bar chart (names vs marks), a line chart (marks), and a histogram (marks distribution) using Pandas built-in `.plot()`.

* **task9.py (Mini Use Case: Sales Data Analysis)**
  Calculates total revenue, average daily revenue, highest revenue day, days where revenue > average, and plots revenue vs day.

* **main.py & assignment10.ipynb**
  Contains all 9 tasks solved sequentially in a single Python script and Jupyter Notebook.

## How to Run

Run all tasks together:

```bash
python main.py
```

Or run each file individually:

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
python task6.py
python task7.py
python task8.py
python task9.py
```
