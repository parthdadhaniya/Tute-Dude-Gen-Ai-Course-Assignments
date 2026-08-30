# shop_package/discount.py
# Functions for applying percentage and flat discounts

def apply_discount(price, percentage):
    """Calculates final price after applying percentage discount."""
    # percentage discount formula: price - (price * (percentage / 100))
    discount_amount = price * (percentage / 100.0)
    final_price = price - discount_amount
    return final_price

def flat_discount(price):
    """Applies a flat discount of 50 rupees/dollars."""
    # flat discount of 50
    # check if price is less than 50 just to avoid negative values
    if price < 50:
        return 0.0
    return price - 50

# quick module check
if __name__ == "__main__":
    print("1000 with 15% off:", apply_discount(1000, 15))
    print("200 with flat discount:", flat_discount(200))
