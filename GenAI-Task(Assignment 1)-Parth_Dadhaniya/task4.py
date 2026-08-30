# Task 4: Combined Operations
# Author: Parth Dadhaniya

# Data given from previous tasks
products = [
    "Laptop", "Smartphone", "Headphones", "Wireless Mouse",
    "Keyboard", "Smartwatch", "USB-C Cable", "Gaming Monitor"
]

categories = [
    "Electronics", "Electronics", "Audio", "Accessories",
    "Accessories", "Wearables", "Accessories", "Electronics"
]

price_dict = {
    "Laptop": 949.99,
    "Smartphone": 699.99,
    "Headphones": 149.99,
    "Wireless Mouse": 29.99,
    "Keyboard": 49.99,
    "Smartwatch": 199.99,
    "USB-C Cable": 14.99,
    "Gaming Monitor": 299.99
}

# 1. Create catalog: a list of tuples containing (product_name, price, category)
catalog = []
for i in range(len(products)):
    p_name = products[i]
    p_category = categories[i]
    p_price = price_dict[p_name]
    catalog.append((p_name, p_price, p_category))

print("Catalog (List of Tuples):")
for item in catalog:
    print(" ", item)

# 2. Map category -> list of product names using dictionary
category_to_products = {}
for item in catalog:
    p_name = item[0]
    p_cat = item[2]
    
    if p_cat not in category_to_products:
        category_to_products[p_cat] = []
        
    category_to_products[p_cat].append(p_name)

print("\nCategory to Products Mapping:")
for cat, prod_list in category_to_products.items():
    print(f"  {cat}: {prod_list}")

# 3. Find category with maximum number of products using a simple for loop
max_cat = None
max_count = 0

for cat, prod_list in category_to_products.items():
    if len(prod_list) > max_count:
        max_count = len(prod_list)
        max_cat = cat

print(f"\nCategory with maximum products: '{max_cat}' ({max_count} products)")
print(f"Products in '{max_cat}': {category_to_products[max_cat]}")
