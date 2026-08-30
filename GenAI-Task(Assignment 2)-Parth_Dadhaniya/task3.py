# Task 3: User Menu (while loop + break/continue)
# Interactive order management system

orders = []

while True:
    print("\n--- ORDER MANAGEMENT MENU ---")
    print("1. Add order amount")
    print("2. View orders summary")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == '1':
        # Add order amount with try/except validation
        user_val = input("Enter order amount to add: ").strip()
        try:
            amount = float(user_val)
            if amount < 0:
                print("Order amount cannot be negative!")
                continue
            orders.append(amount)
            print(f"Order of ${amount:.2f} added successfully.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

    elif choice == '2':
        # Display summary of recorded orders
        if not orders:
            print("No orders added yet.")
            continue

        print("\n--- Orders Summary ---")
        total_revenue = 0.0

        for order in orders:
            if order >= 2000:
                discount_percent = 15
            elif order >= 1500:
                discount_percent = 10
            elif order >= 1000:
                discount_percent = 7
            else:
                discount_percent = 0

            discount_amount = order * (discount_percent / 100)
            final_amount = order - discount_amount
            total_revenue += final_amount

            print(f"Order: ${order:.2f} | Discount: {discount_percent}% | Final: ${final_amount:.2f}")

        print(f"Total Revenue: ${total_revenue:.2f}")

    elif choice in ['3', 'q', 'Q']:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue
