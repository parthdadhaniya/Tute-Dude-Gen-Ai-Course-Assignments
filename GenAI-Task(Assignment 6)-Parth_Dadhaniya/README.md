# Assignment 6: Python Exception Handling

**Student Name:** Parth Dadhaniya  
**Topic:** Exception Handling in Python (`try`, `except`, `else`, `finally`, `raise`, and Custom Exceptions)

---

## Overview

This repository contains my resubmitted code for **Assignment 6: Exception Handling**, updated based on mentor feedback. The goal of this assignment is to understand how exception handling works in Python, why specific error types exist, and how to write clear, error-resistant code.

---

## Key Task Solutions & Feedback Fixes

### 1. Task 1: Safe Division Utility (`task1_safe_division.py`)
- **Concepts:** `try`, `except`, `else`, and `finally`.
- **Exceptions Handled:** `ValueError` (for non-numeric inputs) and `ZeroDivisionError` (division by zero).
- **Feedback Fix:** The `finally` block now prints the exact required string `"Operation Complete"`.

### 2. Task 2: Bill Calculator (`task2_bill_calculator.py`)
- **Concept:** Exception Propagation (`raise` keyword).
- **Exceptions Handled:** `TypeError` (for non-numeric list items) and `ValueError` (for negative prices).
- **Explanation:** The helper function `check_item_price()` raises errors when invalid values are encountered. Instead of swallowing errors inside the helper, `raise` bubbles the exception up to `calculate_bill()`, where the caller handles it and skips the item.

### 3. Task 3: Age Validator (`task3_age_validator.py`)
- **Concept:** Separating type conversion errors from validation logic.
- **Exceptions Handled:** `ValueError` from `int()` conversion vs `ValueError` raised by `validate_age_range()` (checking age between 1 and 120).
- **Explanation:** Separating string conversion from range checking allows the program to report distinct, accurate feedback for invalid input formats vs invalid age values.

### 4. Task 4: Safe File Reader Utility (`task4_file_reader.py`)
- **Concepts:** File exception handling, line-by-line reading, and resource cleanup with `finally`.
- **Exceptions Handled:** `FileNotFoundError` and `PermissionError`.
- **Feedback Fix (CRITICAL):** Updated the file reading logic to print **only the first 3 lines** of the file (using `readline()` in a loop up to 3 times) instead of reading the entire file content with `read()`.

### 5. Task 5: Safe Shopping Cart (`task5_safe_shopping_cart.py`)
- **Concept:** Custom exception classes inheriting from `Exception`.
- **Exceptions Handled:** `ValueError` for float input errors and custom `NegativePriceError` for negative prices.
- **Explanation:** Created `NegativePriceError` to catch negative price entries specifically and display custom messages.

---

## How to Run

You can run the interactive main runner or test each task script individually.

### Run Main Menu
```bash
python main.py
```

### Run Individual Task Scripts
```bash
# Task 1: Safe Division Utility
python task1_safe_division.py

# Task 2: Bill Calculator (Exception Propagation)
python task2_bill_calculator.py

# Task 3: Age Validator
python task3_age_validator.py

# Task 4: File Reader Utility (Reads 3 Lines)
python task4_file_reader.py

# Task 5: Safe Shopping Cart (Custom Exception)
python task5_safe_shopping_cart.py
```

---

## Student Learning Notes & Resubmission Summary

In this revision:
1. **Fixed Task 4 Line Limit:** I changed `file.read()` to a loop reading 3 lines with `file_obj.readline()`. Testing with `sample.txt` confirmed that line 4 is ignored, fulfilling the requirement.
2. **Fixed Task 1 Completion Output:** Updated the `finally` block in `task1_safe_division.py` to print `"Operation Complete"` exactly.
3. **Authentic Code & Comments:** I simplified all functions, removed overly verbose AI-style comments, and rewrote the comments in my own words to clearly reflect my understanding of exception handling concepts.
