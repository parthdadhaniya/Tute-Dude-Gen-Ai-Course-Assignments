# Part 1: Storing Data in SQLite Database (Tasks 1 & 2)
# Student: Parth Dadhaniya

import os
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), "company.db")


def create_database():
    """Task 1: Create SQLite database and tables."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Table 1: employees
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
    """)

    # Table 2: sales
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        amount INTEGER NOT NULL,
        sale_date TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(id)
    )
    """)

    conn.commit()
    conn.close()
    print("Database 'company.db' and tables created successfully.")


def insert_sample_data():
    """Task 2: Insert at least 10 records into each table."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear existing rows to avoid duplicate primary key on rerun
    cursor.execute("DELETE FROM sales")
    cursor.execute("DELETE FROM employees")

    # 10 employees
    employees = [
        (1, "Alice Johnson", "Engineering", 95000),
        (2, "Bob Smith", "Sales", 65000),
        (3, "Charlie Brown", "Marketing", 58000),
        (4, "Diana Prince", "Engineering", 105000),
        (5, "Evan Wright", "Sales", 72000),
        (6, "Fiona Gallagher", "HR", 60000),
        (7, "George Clark", "Marketing", 62000),
        (8, "Hannah Abbott", "Engineering", 88000),
        (9, "Ian Malcolm", "Sales", 81000),
        (10, "Parth Dadhaniya", "AI Research", 120000)
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees)

    # 10 sales records
    sales = [
        (101, 2, 4500, "2026-01-15"),
        (102, 5, 6200, "2026-01-18"),
        (103, 9, 7800, "2026-01-22"),
        (104, 2, 3100, "2026-02-05"),
        (105, 5, 5400, "2026-02-12"),
        (106, 9, 9100, "2026-02-20"),
        (107, 2, 4900, "2026-03-02"),
        (108, 5, 6800, "2026-03-10"),
        (109, 9, 8300, "2026-03-15"),
        (110, 2, 5200, "2026-03-22")
    ]
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", sales)

    conn.commit()
    conn.close()
    print("Inserted 10 employees and 10 sales records.")


def verify_database():
    """Task 2: Run basic SQL queries to verify insertion."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees")
    emp_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sales")
    sales_count = cursor.fetchone()[0]

    cursor.execute("SELECT name, department, salary FROM employees ORDER BY salary DESC LIMIT 1")
    top_earner = cursor.fetchone()

    cursor.execute("SELECT SUM(amount) FROM sales")
    total_sales = cursor.fetchone()[0]

    conn.close()

    print(f"\nVerification Results:")
    print(f"- Total employees in DB : {emp_count}")
    print(f"- Total sales in DB     : {sales_count}")
    print(f"- Highest paid employee : {top_earner[0]} ({top_earner[1]}) with salary ${top_earner[2]:,}")
    print(f"- Total sales amount    : ${total_sales:,}")


def main():
    print("--- Tasks 1 & 2: SQLite Database Setup & Verification ---")
    create_database()
    insert_sample_data()
    verify_database()


if __name__ == "__main__":
    main()
