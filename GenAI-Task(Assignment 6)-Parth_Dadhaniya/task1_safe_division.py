# Task 1: Safe Division Program
# Demonstrating try, except, else, and finally blocks in Python

def safe_division():
    print("--- Safe Division Program ---")
    try:
        num_str = input("Enter numerator: ")
        den_str = input("Enter denominator: ")
        
        num = float(num_str)
        den = float(den_str)
        
        result = num / den
        
    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        
    else:
        # Runs only if no exception occurred in try block
        print(f"Result: {num} / {den} = {result}")
        
    finally:
        # Always runs regardless of errors
        print("Operation Complete")

if __name__ == "__main__":
    safe_division()
