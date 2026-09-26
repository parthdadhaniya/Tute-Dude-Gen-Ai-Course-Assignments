import sqlite3
import pandas as pd

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

# clear and insert 5 records
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

df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df)
conn.close()
