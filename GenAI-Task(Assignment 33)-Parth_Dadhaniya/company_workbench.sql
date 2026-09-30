-- Assignment 33: MySQL Workbench Database Script
-- Student: Parth Dadhaniya
-- Database: company_db

CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

-- 1. Table: employees
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary INT NOT NULL
);

-- 2. Table: sales
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    amount INT NOT NULL,
    sale_date DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
);

-- 3. Insert Employees (10 Records)
INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Alice Johnson', 'Engineering', 95000),
(2, 'Bob Smith', 'Sales', 65000),
(3, 'Charlie Brown', 'Marketing', 58000),
(4, 'Diana Prince', 'Engineering', 105000),
(5, 'Evan Wright', 'Sales', 72000),
(6, 'Fiona Gallagher', 'HR', 60000),
(7, 'George Clark', 'Marketing', 62000),
(8, 'Hannah Abbott', 'Engineering', 88000),
(9, 'Ian Malcolm', 'Sales', 81000),
(10, 'Parth Dadhaniya', 'AI Research', 120000);

-- 4. Insert Sales (10 Records)
INSERT INTO sales (sale_id, employee_id, amount, sale_date) VALUES
(101, 2, 4500, '2026-01-15'),
(102, 5, 6200, '2026-01-18'),
(103, 9, 7800, '2026-01-22'),
(104, 2, 3100, '2026-02-05'),
(105, 5, 5400, '2026-02-12'),
(106, 9, 9100, '2026-02-20'),
(107, 2, 4900, '2026-03-02'),
(108, 5, 6800, '2026-03-10'),
(109, 9, 8300, '2026-03-15'),
(110, 2, 5200, '2026-03-22');

-- Verification Queries for Workbench
SELECT * FROM employees;
SELECT * FROM sales;
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary FROM employees GROUP BY department;
SELECT SUM(amount) as total_sales FROM sales;
