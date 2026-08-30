# Task 2: Process Multiple Orders (for loop)
# Process a list of orders using a for loop and calculate total revenue

orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0.0

print("Orders Processing Summary:")
print("----------------------------------------")

for order in orders:
    # Determine discount percentage based on order amount
    if order >= 2000:
        discount_percent = 15
    elif order >= 1500:
        discount_percent = 10
    elif order >= 1000:
        discount_percent = 7
    else:
        discount_percent = 0

    # Calculate discount amount and final order total
    discount_amount = order * (discount_percent / 100)
    final_amount = order - discount_amount

    # Accumulate total revenue
    total_revenue += final_amount

    print(f"Order: ${order} | Discount: {discount_percent}% | Final Amount: ${final_amount:.2f}")

print("----------------------------------------")
print(f"Total Revenue: ${total_revenue:.2f}")
