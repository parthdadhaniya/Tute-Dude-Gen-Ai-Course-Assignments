# Task 1: Discount Rules (if / elif / else)
# Program to calculate discount and total amount based on user input order amount

try:
    order_amount = float(input("Enter order amount: "))

    if order_amount < 0:
        print("Invalid input! Order amount cannot be negative.")
    else:
        # Determine discount percentage based on order amount
        if order_amount >= 2000:
            discount_percent = 15
        elif order_amount >= 1500:
            discount_percent = 10
        elif order_amount >= 1000:
            discount_percent = 7
        else:
            discount_percent = 0

        # Calculate discount amount and final total
        discount_amount = order_amount * (discount_percent / 100)
        final_total = order_amount - discount_amount

        # Display output summary
        print(f"\nOriginal Order Amount: ${order_amount:.2f}")
        print(f"Discount Applied: {discount_percent}% (${discount_amount:.2f})")
        print(f"Final Amount to Pay: ${final_total:.2f}")

except ValueError:
    print("Invalid input! Please enter a valid numeric order amount.")
