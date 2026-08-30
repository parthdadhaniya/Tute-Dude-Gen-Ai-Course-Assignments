# shop_package/billing.py
# Functions for billing and tax calculation

def calculate_total(item_prices):
    """Takes a list of item prices and returns total sum."""
    # print("DEBUG: item list = ", item_prices)
    total = 0.0
    for price in item_prices:
        total += price
    return total

def apply_tax(amount, tax_rate=5.0):
    """Applies tax percentage to given amount. Default tax rate is 5%."""
    tax_added = amount * (tax_rate / 100.0)
    return amount + tax_added

if __name__ == "__main__":
    items = [150.0, 250.0, 100.0]
    subtotal = calculate_total(items)
    print("Subtotal:", subtotal)
    print("Total with tax:", apply_tax(subtotal))
