# Math utility functions module
# Created by Parth Dadhaniya for Assignment 5

def add(num1, num2):
    # simple helper to add 2 numbers
    return num1 + num2

def subtract(num1, num2):
    # subtract num2 from num1
    return num1 - num2

def square(val):
    # calculate square of number
    # note: val ** 2 is faster than val * val
    return val ** 2

# quick manual testing if run directly
if __name__ == "__main__":
    print("Testing math_utils functions:")
    print("Add 5 + 3:", add(5, 3))
    print("Subtract 10 - 4:", subtract(10, 4))
    print("Square of 6:", square(6))
