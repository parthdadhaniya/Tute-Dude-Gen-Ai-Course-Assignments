# Assignment 1: Python Data Structures

**Student Name:** Parth Dadhaniya  
**Course:** GenAI - TuteDude  

## Overview
This repository contains my submission for Assignment 1 on **Python Data Structures**. The tasks demonstrate working with core built-in Python data structures including **Lists**, **Tuples**, **Sets**, and **Dictionaries** using an e-commerce product catalog example.

---

## File Breakdown & Tasks

| File Name | Task Name | What it Does |
| :--- | :--- | :--- |
| `task1.py` | Task 1: Product Collections | Creates a product list and sample product tuple. Demonstrates list indexing, appending items, and modifying tuples by temporarily converting to lists. |
| `task2.py` | Task 2: Categories | Converts a category list to a set to remove duplicates. Demonstrates adding new items, handling duplicate additions, checking set membership with `in`, and counting total unique items. |
| `task3.py` | Task 3: Product Pricing | Uses a dictionary to store product-price pairs. Performs operations like adding items, updating prices, safe deletion (`in` check), calculating average price, and finding max/min prices using a simple loop. |
| `task4.py` | Task 4: Combined Operations | Combines lists, tuples, and dictionaries to build a complete product catalog list of tuples. Groups products by category in a dictionary and finds the category with the maximum items using simple loops. |
| `main.py` | Main Execution Script | Executes all 4 tasks sequentially with visual separators for easy review. |

---

## How to Run

### Execute All Tasks at Once:
Run the `main.py` file from your terminal:
```bash
python3 main.py
```

### Execute Individual Tasks:
You can also run any specific task file directly:
```bash
python3 task1.py
python3 task2.py
python3 task3.py
python3 task4.py
```

---

## Key Learning Outcomes
- **Lists:** Ordered, mutable collections ideal for storing sequences of products.
- **Tuples:** Ordered, immutable collections suitable for grouping fixed product details `(name, price, category)`.
- **Sets:** Unordered collections of unique elements, perfect for filtering duplicate categories.
- **Dictionaries:** Key-value mappings useful for fast lookups by product name or grouping lists of products by category.
