# Assignment 4 - Python File Handling

This project contains my solution for Python File Handling operations (reading, writing, appending files, safe checking, and exporting reports).

## Files Overview

- `main.py`: Runs all 7 tasks sequentially with input prompts.
- `task1.py`: Writes initial sales numbers to `sales_data.txt` line by line and optionally to `sales_data_csv.txt` in comma-separated format.
- `task2.py`: Demonstrates reading file contents using `.read()`, `.readline()`, and `.readlines()`.
- `task3.py`: Appends new sales figures to `sales_data.txt` and prints the total number of lines in the file.
- `task4.py`: Calculates total sales, highest sale, lowest sale, and average sale from `sales_data.txt`.
- `task5.py`: Asks for product details (name and price) from user input and writes them to `products.txt`.
- `task6.py`: Prompts for a filename and uses `os.path.exists()` to safely open and read it.
- `task7.py`: Calculates discounted prices for hardware items, writes a report with a summary block (total items and average price) to `discount_report.txt`, and displays it.

## How to Run

To run all tasks together:
```bash
python main.py
```

To run tasks individually:
```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
python task6.py
python task7.py
```

