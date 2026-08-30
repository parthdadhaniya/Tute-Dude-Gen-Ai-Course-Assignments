# Assignment 3: Python Functions & Utilities

This repository contains the solution for **Assignment 3 (Python Functions)**. The assignment covers user-defined functions, recursive functions, lambda expressions, built-in functional utilities (`map` and `filter`), combined functional workflows, and an interactive menu program.

---

## 📁 File Overview

- **`task1.py`**: Basic function (`apply_discount`) to calculate price after discount with a default discount of 5%.
- **`task2.py`**: Recursive function (`factorial`) to calculate the factorial of a number.
- **`task3.py`**: Lambda function (`gst`) to calculate price after applying 18% GST.
- **`task4.py`**: Using `map()` with lambda to apply GST to a list of prices (`[100, 250, 400, 1200, 50]`).
- **`task5.py`**: Using `filter()` with lambda to filter prices greater than 500 (`[100, 250, 400, 1200, 50, 2000, 850]`).
- **`task6.py`**: Combined function (`process_prices`) applying a 10% discount and filtering prices > 300 for `[500, 900, 50, 750]`.
- **`task7.py`**: Interactive CLI program with a menu to add prices, calculate average price, and find the highest price.
- **`main.py`**: Master runner script executing Tasks 1 to 6 sequentially.

---

## 🚀 How to Run

### Requirements
- Python 3.x installed on your system.

### Running Individual Tasks
To run any specific task script, open your terminal in the project directory and run:

```bash
python3 task1.py
python3 task2.py
python3 task3.py
python3 task4.py
python3 task5.py
python3 task6.py
python3 task7.py
```

### Running All Tasks at Once
To run Tasks 1 through 6 sequentially using the master script:

```bash
python3 main.py
```

### Running the Interactive Menu (Task 7)
Task 7 provides an interactive menu. Execute:

```bash
python3 task7.py
```
Follow the on-screen menu options:
1. **Option 1**: Add a price
2. **Option 2**: Show average price
3. **Option 3**: Show highest price
4. **Option 4**: Quit application
