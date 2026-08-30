# Task 1: Product Collections (Lists & Tuples)
# Author: Parth Dadhaniya

# 1. List of product names (at least 6 products)
products = ["Laptop", "Smartphone", "Headphones", "Wireless Mouse", "Keyboard", "Smartwatch"]
print("Initial Products List:")
print(products)

# 2. Tuple storing (product_name, price, category)
sample_product = ("Laptop", 999.99, "Electronics")
print("\nSample Product Tuple:")
print(sample_product)

# 3. Accessing 2nd product (index 1) and last product (index -1)
print("\n2nd product:", products[1])
print("Last product:", products[-1])

# 4. Adding 2 new products to list using append()
products.append("USB-C Cable")
products.append("Gaming Monitor")
print("\nProducts list after adding new items:")
print(products)

# Extra part: Since tuples cannot be changed directly (immutable), 
# I convert it to a list first, update the price, then convert back to tuple.
temp_list = list(sample_product)
temp_list[1] = 899.99
sample_product = tuple(temp_list)
print("\nUpdated Sample Product Tuple after price change:")
print(sample_product)
