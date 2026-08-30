# Task 2: Categories (Sets)
# Author: Parth Dadhaniya

# List of categories matching products list
categories = [
    "Electronics", "Electronics", "Audio", "Accessories",
    "Accessories", "Wearables", "Accessories", "Electronics"
]

# 1. Convert categories list to set (sets remove duplicate items)
categories_set = set(categories)
print("Initial Categories Set:")
print(categories_set)

# 2. Demonstrate adding a new category
print("\nAdding a new category 'Gaming'...")
categories_set.add("Gaming")
print("Categories Set after adding 'Gaming':", categories_set)

# Trying to add duplicate category
print("\nTrying to add duplicate category 'Electronics'...")
categories_set.add("Electronics")
print("Categories Set after adding duplicate 'Electronics':", categories_set)

# 3. Check if specific category exists in set (using 'in' keyword)
cat1 = "Audio"
cat2 = "Home Appliances"

print("\nIs 'Audio' in categories_set?:", cat1 in categories_set)
print("Is 'Home Appliances' in categories_set?:", cat2 in categories_set)

# Extra part: Total count of unique categories
print("\nTotal unique categories count:", len(categories_set))
