# Task 3: Age Validator
# Handling type conversion ValueError separately from age range ValueError

def validate_age_range(age):
    # Check if age is within reasonable bounds (1 to 120)
    if age < 1 or age > 120:
        raise ValueError(f"Age {age} is invalid. Age must be between 1 and 120.")
    return age

def main():
    print("--- Age Validator Program ---")
    user_input = input("Enter your age: ").strip()

    # Step 1: Handle string conversion to integer
    try:
        age_num = int(user_input)
    except ValueError:
        print("Input Error: Please enter a valid whole number (e.g. 25).")
        return

    # Step 2: Handle age range validation separately
    try:
        valid_age = validate_age_range(age_num)
        print(f"Success: Validated age is {valid_age}.")
    except ValueError as e:
        print(f"Validation Error: {e}")

if __name__ == "__main__":
    main()
