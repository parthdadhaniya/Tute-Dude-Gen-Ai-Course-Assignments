# Assignment 3: Functions (User-Defined, Recursive, Lambda, Map, Filter)
# Master runner file executing all task modules sequentially.

import task1
import task2
import task3
import task4
import task5
import task6

def run_all_tasks():
    print("=" * 60)
    print("   ASSIGNMENT 3: PYTHON FUNCTIONS & UTILITIES SOLUTION   ")
    print("=" * 60)
    print()

    # --- TASK 1 ---
    print("[TASK 1] Basic Function: Price After Discount")
    p1 = task1.apply_discount(1000, 10)
    p2 = task1.apply_discount(500)
    print(f"  - apply_discount(1000, 10) => {p1}")
    print(f"  - apply_discount(500)       => {p2} (using default 5%)")
    print()

    # --- TASK 2 ---
    print("[TASK 2] Recursive Function: Factorial Utility")
    f1 = task2.factorial(5)
    f2 = task2.factorial(0)
    print(f"  - factorial(5)  => {f1}")
    print(f"  - factorial(0)  => {f2}")
    print()

    # --- TASK 3 ---
    print("[TASK 3] Lambda Function: GST Calculator")
    g1 = task3.gst(100)
    print(f"  - GST (18%) on 100        => {g1}")
    print()

    # --- TASK 4 ---
    print("[TASK 4] Using map(): Apply GST to List of Prices")
    print(f"  - Original Prices : {task4.prices}")
    print(f"  - Prices after GST: {task4.prices_with_gst}")
    print()

    # --- TASK 5 ---
    print("[TASK 5] Using filter(): Filter Expensive Products")
    print(f"  - Original Prices       : {task5.prices}")
    print(f"  - Expensive (> 500)     : {task5.expensive_prices}")
    print(f"  - Affordable (<= 500)   : {task5.affordable_prices}")
    print()

    # --- TASK 6 ---
    print("[TASK 6] Combined Utility Function")
    input_p = [500, 900, 50, 750]
    disc_p, filt_p = task6.process_prices(input_p)
    print(f"  - Input Prices                : {input_p}")
    print(f"  - Discounted Prices (10% off) : {disc_p}")
    print(f"  - Filtered Prices (> 300)     : {filt_p}")
    print()

    print("=" * 60)
    print("All tasks 1-6 executed successfully!")
    print("To run Task 7 interactive menu, execute 'python3 task7.py'.")
    print("=" * 60)

if __name__ == "__main__":
    run_all_tasks()

