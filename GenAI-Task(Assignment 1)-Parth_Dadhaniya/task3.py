# Task 3: Product Pricing (Dictionaries)
# Author: Parth Dadhaniya

# 1. Create price_dict dictionary (product name -> price)
price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 149.99,
    "Wireless Mouse": 29.99,
    "Keyboard": 49.99,
    "Smartwatch": 199.99,
    "USB-C Cable": 14.99,
    "Gaming Monitor": 299.99
}

print("Initial Price Dictionary:")
print(price_dict)

# 2a. Add a new product to price_dict
price_dict["Webcam"] = 59.99
print("\nAfter adding 'Webcam':")
print(price_dict)

# 2b. Update the price of an existing product
price_dict["Laptop"] = 949.99
print("\nAfter updating price of 'Laptop':")
print(price_dict)

# 2c. Safely remove a product by checking if it exists first
prod_to_remove = "Headphones"
if prod_to_remove in price_dict:
    removed_price = price_dict.pop(prod_to_remove)
    print(f"\nSuccessfully removed '{prod_to_remove}' (Price: ${removed_price})")

# Test removing a product that doesn't exist
missing_prod = "Desk Lamp"
if missing_prod in price_dict:
    price_dict.pop(missing_prod)
else:
    print(f"Safe check: '{missing_prod}' is not in dictionary, nothing to remove.")

# 2d. Calculate average price using a loop and len()
total_sum = 0.0
for price in price_dict.values():
    total_sum += price

avg_price = total_sum / len(price_dict)
print(f"\nAverage Product Price: ${avg_price:.2f}")

# Extra part: Find max and min price using a simple for loop
highest_product = None
highest_price = -1.0

lowest_product = None
lowest_price = 999999.0

for product, price in price_dict.items():
    if price > highest_price:
        highest_price = price
        highest_product = product
        
    if price < lowest_price:
        lowest_price = price
        lowest_product = product

print(f"\nProduct with Maximum Price: '{highest_product}' (${highest_price})")
print(f"Product with Minimum Price: '{lowest_product}' (${lowest_price})")
