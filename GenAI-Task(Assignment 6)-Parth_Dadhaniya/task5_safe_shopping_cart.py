# Task 5: Safe Shopping Cart
# Demonstrating custom exception class NegativePriceError

class NegativePriceError(Exception):
    # Custom exception for negative prices
    def __init__(self, price):
        self.price = price
        super().__init__(f"Negative price '${price:.2f}' is invalid.")

def run_shopping_cart():
    cart = []
    print("--- Safe Shopping Cart System ---")
    print("Enter item prices. Type 'q' or 'quit' when finished.\n")

    while True:
        user_input = input("Enter item price: ").strip()

        if user_input.lower() in ['q', 'quit']:
            break

        try:
            # 1. Convert to float (catches ValueError if text)
            price = float(user_input)

            # 2. Check for negative price using custom exception
            if price < 0:
                raise NegativePriceError(price)

            cart.append(price)
            print(f"  Added ${price:.2f} to cart.")

        except ValueError:
            print("  [Input Error]: Please enter a valid numerical price.")

        except NegativePriceError as err:
            print(f"  [Custom Exception]: {err}")

    # Summary
    print("\n--- Shopping Cart Summary ---")
    if cart:
        for i, item_price in enumerate(cart, 1):
            print(f"Item {i}: ${item_price:.2f}")
        total = sum(cart)
        print("-" * 30)
        print(f"Total Items: {len(cart)}")
        print(f"Total Bill: ${total:.2f}")
    else:
        print("Your cart is empty.")

if __name__ == "__main__":
    run_shopping_cart()
