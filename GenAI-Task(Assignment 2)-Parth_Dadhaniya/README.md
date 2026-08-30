# GenAI-Task (Assignment 2) — Control Flow & Loops

**Student Name:** Parth Dadhaniya  
**Course:** Python Programming / GenAI  
**Topic:** Conditionals, For Loops, While Loops, Loop Control (`break`/`continue`), and Numeric Input Validation (`try/except`)

---

## Overview

This repository contains the Python scripts for Assignment 2. The assignment demonstrates fundamental control flow and iteration techniques in Python, including conditional logic (`if`/`elif`/`else`), sequence iteration using `for` loops, interactive menu loops using `while True`, loop control flow (`break` and `continue`), and robust user input validation using `try/except ValueError` blocks.

---

## Task Summaries

### Task 1: Discount Rules (`task1.py`)
- **Description:** Takes an order amount from the user, validates it using `try/except ValueError` to support float values and handle invalid input gracefully, applies tiered discount logic, and displays the order summary.
- **Discount Rules:**
  - Order amount ≥ $2000 → 15% discount
  - Order amount ≥ $1500 → 10% discount
  - Order amount ≥ $1000 → 7% discount
  - Order amount < $1000 → 0% discount

### Task 2: Process Multiple Orders (`task2.py`)
- **Description:** Iterates over a pre-defined list of order amounts (`[1200, 2500, 800, 1750, 3000]`) using a `for` loop.
- **Output:** Calculates the applicable discount for each order item, computes final amounts, and displays total accumulated revenue.

### Task 3: User Menu (`task3.py`)
- **Description:** Implements an interactive menu system using a `while True` loop and control statements (`break`/`continue`).
- **Features:**
  1. Add new order amounts (with `try/except ValueError` input validation).
  2. View summary table of all recorded orders and calculated total revenue.
  3. Quit the program.

### Task 4: Loop Control with Conditions (`task4.py`)
- **Description:** Processes daily sales data (`[200, 150, 0, 400, 50, -1, 300]`) using loop control statements.
- **Logic:**
  - If sale amount is `0` (no sales day): Skips addition using `continue`.
  - If sale amount is `-1` (corrupted data): Stops loop execution using `break`.
  - Displays running total for valid positive sales.

---

## How to Run

Make sure Python 3 is installed on your system. Open terminal or command line in the project folder and execute the commands:

```bash
# Run Task 1 (Interactive Input & Discount Logic)
python task1.py

# Run Task 2 (For Loop List Processing)
python task2.py

# Run Task 3 (Interactive Menu System)
python task3.py

# Run Task 4 (Loop Control with break/continue)
python task4.py
```

---

## Core Concepts Demonstrated
- **Conditional Branching:** `if`, `elif`, and `else` blocks.
- **Loop Iteration:** `for` loop and `while True` infinite loops.
- **Loop Control:** `break` to exit loops early and `continue` to skip iterations.
- **Input Validation:** `try / except ValueError` error handling for reliable number conversion.
- **Data Structures:** List manipulation with `.append()`.
