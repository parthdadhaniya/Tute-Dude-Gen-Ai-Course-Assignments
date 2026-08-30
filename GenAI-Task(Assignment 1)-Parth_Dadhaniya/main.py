"""
Assignment 1: Python - Data Structures
Developer: Parth Dadhaniya

Main script to run all individual tasks:
1. Task 1: Product Collections (Lists & Tuples)
2. Task 2: Categories (Sets)
3. Task 3: Product Pricing (Dictionaries)
4. Task 4: Combined Operations
"""

def task1():
    print("=" * 50)
    print("TASK 1: Product Collections (Lists & Tuples)")
    print("=" * 50)
    
    # List of 6 products
    products = ["Laptop", "Smartphone", "Headphones", "Wireless Mouse", "Keyboard", "Smartwatch"]
    print("Initial Products List:", products)
    
    # Tuple of sample product details
    sample_product = ("Laptop", 999.99, "Electronics")
    print("Sample Product (Tuple):", sample_product)
    
    # Accessing items by index
    print("\n2nd product:", products[1])
    print("Last product:", products[-1])
    
    # Appending new items
    products.append("USB-C Cable")
    products.append("Gaming Monitor")
    print("\nUpdated Products List:", products)
    
    # Tuple modification via temporary list
    temp_list = list(sample_product)
    temp_list[1] = 899.99
    sample_product = tuple(temp_list)
    print("\nUpdated Sample Product (Tuple):", sample_product)
    print()


def task2():
    print("=" * 50)
    print("TASK 2: Categories (Sets)")
    print("=" * 50)
    
    categories = [
        "Electronics", "Electronics", "Audio", "Accessories",
        "Accessories", "Wearables", "Accessories", "Electronics"
    ]
    
    # Creating set from list
    categories_set = set(categories)
    print("Initial Categories Set:", categories_set)
    
    # Adding items to set
    categories_set.add("Gaming")
    print("\nAfter adding 'Gaming':", categories_set)
    
    # Testing duplicate addition
    categories_set.add("Electronics")
    print("After adding duplicate 'Electronics':", categories_set)
    
    # Set membership checking
    print("\nIs 'Audio' in categories_set?:", "Audio" in categories_set)
    print("Is 'Home Appliances' in categories_set?:", "Home Appliances" in categories_set)
    
    # Unique count
    print("\nTotal Unique Categories:", len(categories_set))
    print()


def task3():
    print("=" * 50)
    print("TASK 3: Product Pricing (Dictionaries)")
    print("=" * 50)
    
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
    
    print("Initial Price Dictionary:", price_dict)
    
    # Adding new item
    price_dict["Webcam"] = 59.99
    print("\nAfter adding 'Webcam':", price_dict)
    
    # Updating existing item price
    price_dict["Laptop"] = 949.99
    print("\nAfter updating 'Laptop' price:", price_dict)
    
    # Safe key removal
    if "Headphones" in price_dict:
        removed_val = price_dict.pop("Headphones")
        print(f"\nRemoved 'Headphones' (Price: ${removed_val})")
        
    if "Desk Lamp" in price_dict:
        price_dict.pop("Desk Lamp")
    else:
        print("Safe check: 'Desk Lamp' does not exist in price_dict.")
        
    # Average price calculation with loop
    total_price = 0.0
    for price in price_dict.values():
        total_price += price
    avg = total_price / len(price_dict)
    print(f"\nAverage Product Price: ${avg:.2f}")
    
    # Finding min and max prices using standard loop
    max_prod = None
    max_p = -1.0
    min_prod = None
    min_p = 999999.0
    
    for prod, price in price_dict.items():
        if price > max_p:
            max_p = price
            max_prod = prod
        if price < min_p:
            min_p = price
            min_prod = prod
            
    print(f"\nMax Price Product: '{max_prod}' (${max_p})")
    print(f"Min Price Product: '{min_prod}' (${min_p})")
    print()


def task4():
    print("=" * 50)
    print("TASK 4: Combined Operations")
    print("=" * 50)
    
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
    
    # Building catalog list of tuples using simple loop
    catalog = []
    for i in range(len(products)):
        p_name = products[i]
        p_cat = categories[i]
        p_price = price_dict[p_name]
        catalog.append((p_name, p_price, p_cat))
        
    print("Catalog List of Tuples:")
    for item in catalog:
        print(" ", item)
        
    # Creating category to product list dictionary
    category_to_products = {}
    for item in catalog:
        name = item[0]
        cat = item[2]
        if cat not in category_to_products:
            category_to_products[cat] = []
        category_to_products[cat].append(name)
        
    print("\nCategory to Products Mapping:")
    for cat, prod_list in category_to_products.items():
        print(f"  {cat}: {prod_list}")
        
    # Finding category with max products using loop (no lambdas)
    max_cat = None
    max_count = 0
    for cat, prod_list in category_to_products.items():
        if len(prod_list) > max_count:
            max_count = len(prod_list)
            max_cat = cat
            
    print(f"\nCategory with maximum products: '{max_cat}' ({max_count} items)")
    print(f"Products in '{max_cat}': {category_to_products[max_cat]}")
    print()


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
