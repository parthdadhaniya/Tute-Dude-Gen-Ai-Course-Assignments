# Task 2: Bill Calculator (Exception Propagation)
# Understanding how 'raise' bubbles errors up to the caller function

def check_item_price(price):
    # Check if item is a number
    if not isinstance(price, (int, float)):
        raise TypeError(f"'{price}' is not a valid numeric price.")
    
    # Check if price is negative
    if price < 0:
        raise ValueError(f"Price '{price}' cannot be negative.")
    
    return float(price)

def calculate_bill():
    prices = [150.0, 450.50, "fifty", 200.0, -75.0, 320.0]
    total_bill = 0.0

    print("--- Processing Bill Items ---")
    print(f"Prices list: {prices}\n")

    for i, item in enumerate(prices, 1):
        print(f"Processing item {i} ({item}):")
        try:
            # Call helper function. If an error is raised inside,
            # it propagates up to this try-except block in calculate_bill()
            valid_price = check_item_price(item)
            total_bill += valid_price
            print(f"  Added ${valid_price:.2f}. Total so far: ${total_bill:.2f}")

        except TypeError as err:
            print(f"  TypeError caught in caller: {err}")
            print("  Skipping item.")

        except ValueError as err:
            print(f"  ValueError caught in caller: {err}")
            print("  Skipping item.")
        
        print("-" * 40)

    print(f"\nFinal Total Bill: ${total_bill:.2f}")

if __name__ == "__main__":
    calculate_bill()
