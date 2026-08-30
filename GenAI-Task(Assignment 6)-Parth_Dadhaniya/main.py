# Assignment 6: Python Exception Handling - Main Runner Script

import task1_safe_division
import task2_bill_calculator
import task3_age_validator
import task4_file_reader
import task5_safe_shopping_cart

def display_menu():
    print("=" * 50)
    print("   ASSIGNMENT 6: EXCEPTION HANDLING MENU   ")
    print("=" * 50)
    print("1. Task 1: Safe Division Utility")
    print("2. Task 2: Bill Calculator (Exception Propagation)")
    print("3. Task 3: Age Validator (Separating ValueError)")
    print("4. Task 4: File Reader (Resource Cleanup)")
    print("5. Task 5: Safe Shopping Cart (Custom Exception)")
    print("6. Exit")
    print("=" * 50)

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-6): ").strip()
        print()

        if choice == '1':
            task1_safe_division.safe_division()
        elif choice == '2':
            task2_bill_calculator.calculate_bill()
        elif choice == '3':
            task3_age_validator.main()
        elif choice == '4':
            task4_file_reader.read_first_three_lines()
        elif choice == '5':
            task5_safe_shopping_cart.run_shopping_cart()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 6.\n")

if __name__ == "__main__":
    main()
