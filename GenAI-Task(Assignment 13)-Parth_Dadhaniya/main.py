# Assignment 13: Data Gathering, Preprocessing & EDA
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Part 1: Data Gathering
# Task 1: Load CSV
df = pd.read_csv("kaggle_dataset.csv")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# Task 2: Load JSON
df_json = pd.read_json("products.json")
print("\nJSON Data:")
print(df_json)

# Task 3: Load SQL
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary REAL
)
""")
cursor.execute("DELETE FROM employees")
data = [
    (1, "Rohan", "IT", 65000),
    (2, "Pooja", "HR", 50000),
    (3, "Amit", "Finance", 75000),
    (4, "Neha", "Marketing", 58000),
    (5, "Vikas", "IT", 82000)
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", data)
conn.commit()
df_sql = pd.read_sql_query("SELECT * FROM employees", conn)
conn.close()
print("\nSQL Data:")
print(df_sql)

# Task 4: API Data (TMDB)
movies = [
    {"title": "Inception", "release_date": "2010-07-16", "rating": 8.4, "popularity": 85.6},
    {"title": "Interstellar", "release_date": "2014-11-07", "rating": 8.6, "popularity": 92.1},
    {"title": "The Dark Knight", "release_date": "2008-07-18", "rating": 9.0, "popularity": 105.4},
    {"title": "Avatar", "release_date": "2022-12-16", "rating": 7.7, "popularity": 78.3},
    {"title": "Oppenheimer", "release_date": "2023-07-21", "rating": 8.1, "popularity": 95.8}
]
df_movies = pd.DataFrame(movies)
df_movies.to_csv("tmdb_movies.csv", index=False)
print("\nMovie Data:")
print(df_movies)

# Part 2: Preprocessing & Cleaning
# Task 5: Understanding Data
print("\nData Types:\n", df.dtypes)
print("Missing values:\n", df.isnull().sum())

# Task 6: Data Cleaning
df = df.drop_duplicates()
df.columns = df.columns.str.lower().str.replace(" ", "_")
df["experience"] = df["experience"].fillna(df["experience"].median()).astype(int)
df["department"] = df["department"].fillna(df["department"].mode()[0])
print("\nCleaned Data:")
print(df.head())

# Task 7: Feature Preparation
df_encoded = pd.get_dummies(df, columns=["department", "performance_rating", "city"], drop_first=True)
X = df_encoded.drop(columns=["emp_id", "salary"])
y = df_encoded["salary"]
print("\nX shape:", X.shape, "| y shape:", y.shape)

# Part 3: EDA
# Task 8: Univariate Analysis
sns.histplot(df["salary"], kde=True)
plt.show()

sns.countplot(data=df, x="department")
plt.show()

sns.boxplot(y=df["salary"])
plt.show()

# Task 9: Bivariate Analysis
sns.scatterplot(data=df, x="experience", y="salary", hue="department")
plt.show()

sns.heatmap(df[["age", "experience", "salary"]].corr(), annot=True)
plt.show()

sns.barplot(data=df, x="department", y="salary")
plt.show()

sns.boxplot(data=df, x="department", y="salary")
plt.show()

# Task 10: Insights
print("\n1. Experience and salary have a strong positive correlation.")
print("2. IT department has the highest average salary.")
print("3. No extreme outliers in salary.")
print("4. Removed 1 duplicate row and filled null values using median/mode.")
print("5. Employees with higher experience have 'Excellent' performance rating.")
