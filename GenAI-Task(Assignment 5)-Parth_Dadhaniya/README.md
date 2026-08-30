# Assignment 5: Python Modules and Packages

**Student Name:** Parth Dadhaniya  
**Course:** GenAI / Python Programming Course  
**Task:** Assignment 5 - Modules and Packages  

---

## 📌 Project Overview

This repository demonstrates practical implementation of Python modules and packages. It breaks down reusable helper functions into custom utility modules (`math_utils.py`, `string_utils.py`) and an organized e-commerce shopping package (`shop_package`).

---

## 📁 Directory Structure

```text
GenAI-Task(Assignment 5)-Parth_Dadhaniya/
│
├── README.md                           # Project documentation & run guide
└── modules_assignment/
    ├── main.py                         # Main execution script testing all modules & packages
    ├── math_utils.py                   # Math functions (add, subtract, square)
    ├── string_utils.py                 # String functions (capitalize_words, reverse_string, word_count)
    └── shop_package/                   # Python package directory
        ├── __init__.py                 # Package initializer
        ├── discount.py                 # Discount calculations (apply_discount, flat_discount)
        └── billing.py                  # Billing calculations (calculate_total, apply_tax)
```

---

## 🚀 How to Run

### Method 1: Running `main.py` directly from the `modules_assignment` folder (Recommended)

1. Open your terminal or shell.
2. Navigate into the `modules_assignment` directory:
   ```bash
   cd modules_assignment
   ```
3. Run the main demonstration script using Python 3:
   ```bash
   python3 main.py
   ```

### Method 2: Running from the root project directory

If you are at the root folder of the project, run:
```bash
python3 modules_assignment/main.py
```

### Method 3: Testing individual modules

You can also run any module directly to execute its built-in self-tests:
```bash
python3 modules_assignment/math_utils.py
python3 modules_assignment/string_utils.py
python3 modules_assignment/shop_package/discount.py
python3 modules_assignment/shop_package/billing.py
```

---

## 📚 Module & Package Breakdown

### 1. `math_utils.py` (Module)
Contains basic mathematical helper functions:
- `add(num1, num2)`: Returns sum of two numbers.
- `subtract(num1, num2)`: Returns difference between two numbers.
- `square(val)`: Returns square of a number.

### 2. `string_utils.py` (Module)
Contains string manipulation utilities:
- `capitalize_words(text)`: Capitalizes the first letter of each word using `.title()`.
- `reverse_string(text)`: Reverses string using Python slice notation `[::-1]`.
- `word_count(text)`: Splits text into words and returns the count.

### 3. `shop_package` (Package)
Demonstrates multi-file Python package organization:
- `__init__.py`: Marks directory as a package and exposes key billing & discount functions.
- `discount.py`: Calculates percentage discounts (`apply_discount`) and fixed amount discounts (`flat_discount`).
- `billing.py`: Calculates cart subtotal (`calculate_total`) and computes tax additions (`apply_tax`).

---

## 💡 Key Learnings & Import Techniques

During this assignment, I practiced multiple ways to import and organize Python code:

1. **Standard Module Import**:
   ```python
   import math_utils
   result = math_utils.add(5, 3)
   ```

2. **Specific Function Import**:
   ```python
   from math_utils import square
   sq = square(4)
   ```

3. **Package Submodule Import with Alias**:
   ```python
   import shop_package.discount as disc
   discounted = disc.apply_discount(1000, 10)
   ```

4. **Direct Import from Package Submodule**:
   ```python
   from shop_package.billing import calculate_total, apply_tax
   total = calculate_total([100, 200])
   ```

---

## 📝 Student Reflection & Troubleshooting Notes

- **Understanding `__init__.py`**: Initially I wondered why `__init__.py` was required in Python package folders. I learned that it runs automatically when the package is imported and allows clean exports of inner submodules.
- **Handling `ModuleNotFoundError`**: When I tried importing `from discount import apply_discount` without referencing `shop_package`, Python raised a `ModuleNotFoundError`. I learned that package submodules must be referenced either via absolute path (`from shop_package.discount ...`) or relative imports (`from .discount ...` inside package modules).
- **Managing `sys.path`**: To make sure `main.py` can be executed regardless of the terminal's working directory, I added `sys.path.append(os.path.dirname(os.path.abspath(__file__)))` at the top of `main.py`.
