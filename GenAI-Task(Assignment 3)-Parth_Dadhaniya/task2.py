# Task 2 - Recursive Function: Factorial Utility

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print("--- Task 2: Factorial Utility ---")
    print("Factorial of 5:", factorial(5))
    print("Factorial of 0:", factorial(0))

