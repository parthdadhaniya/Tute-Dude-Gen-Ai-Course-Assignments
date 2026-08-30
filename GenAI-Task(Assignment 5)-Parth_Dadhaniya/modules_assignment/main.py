"""
Assignment 5: Modules and Packages in Python
Student: Parth Dadhaniya

This script tests the custom modules (math_utils, string_utils) 
and package (shop_package) created for this assignment.
"""

import sys
import os

# Ensure the script directory is in sys.path when running from different paths
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- Task 1: Importing math_utils in 2 different ways ---
# Way 1: Standard import of whole module
import math_utils

# Way 2: Importing specific function directly
from math_utils import square


# --- Task 2: Importing string_utils module ---
import string_utils


# --- Task 3 & 4: Importing from package shop_package ---
# Method 1: Importing sub-module with alias
import shop_package.discount as disc

# Method 2: Importing specific functions directly from package sub-module
from shop_package.billing import calculate_total, apply_tax

# Note: tried doing `from discount import apply_discount` first, but got ModuleNotFoundError!
# Had to specify the package name `shop_package.discount`.


def run_math_demos():
    print("\n--- Task 1: Math Utilities Demo ---")
    val1 = 15
    val2 = 4
    
    # Using math_utils module reference
    sum_result = math_utils.add(val1, val2)
    sub_result = math_utils.subtract(val1, val2)
    print(f"Adding {val1} + {val2} = {sum_result}")
    print(f"Subtracting {val1} - {val2} = {sub_result}")
    
    # Using direct square import
    sq_result = square(6)
    print(f"Square of 6 (via direct function import) = {sq_result}")


def run_string_demos():
    print("\n--- Task 2: String Utilities Demo ---")
    sample_text = "python modules and packages assignment"
    print(f"Original String : '{sample_text}'")
    
    cap_text = string_utils.capitalize_words(sample_text)
    rev_text = string_utils.reverse_string(sample_text)
    count = string_utils.word_count(sample_text)
    
    print(f"Capitalized     : '{cap_text}'")
    print(f"Reversed String : '{rev_text}'")
    print(f"Word Count      : {count}")


def run_shop_package_demos():
    print("\n--- Tasks 3 & 4: Shop Package Demo ---")
    
    # Testing discount submodule via alias 'disc'
    original_price = 1200.0
    discount_pct = 15.0
    discounted = disc.apply_discount(original_price, discount_pct)
    flat_disc_price = disc.flat_discount(original_price)
    
    print(f"Original Item Price : Rs.{original_price:.2f}")
    print(f"After {discount_pct}% Discount  : Rs.{discounted:.2f}")
    print(f"After Flat 50 Discount : Rs.{flat_disc_price:.2f}")
    
    # Testing billing submodule via direct import
    item_prices = [299.0, 499.0, 150.0]
    raw_total = calculate_total(item_prices)
    final_bill = apply_tax(raw_total, tax_rate=5.0)
    
    print("\nShopping Cart Items:", item_prices)
    print(f"Subtotal            : Rs.{raw_total:.2f}")
    print(f"Total with 5% Tax   : Rs.{final_bill:.2f}")


if __name__ == "__main__":
    print("==================================================")
    print("      ASSIGNMENT 5: MODULES & PACKAGES IN PYTHON  ")
    print("==================================================")
    
    run_math_demos()
    run_string_demos()
    run_shop_package_demos()
    
    print("\n==================================================")
    print(" All module and package tests completed successfully!")
    print("==================================================")
