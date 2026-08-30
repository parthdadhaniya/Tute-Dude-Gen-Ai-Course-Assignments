# Task 7 - Mini Project: Simple Inventory System

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price

    def get_info(self):
        print(f"Name: {self.name} | Category: {self.category} | Price: {self.get_price()}")

    def __str__(self):
        return f"Product({self.name}, {self.get_price()}, {self.category})"

    def __add__(self, other):
        return self.get_price() + other.get_price()


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Added product:", product.name)

    def remove_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                self.products.remove(p)
                print("Removed product:", name)
                return
        print("Product not found!")

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.get_price()
        return total

    def show_all_products(self):
        print("\n--- All Products in Inventory ---")
        for p in self.products:
            p.get_info()


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name=None, price=None, category=None):
        if name is None or price is None or category is None:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category = input("Enter product category: ")

        p = Product(name, price, category)
        self.inventory.add_product(p)

    def show_summary(self):
        print("\n=============================")
        print("Store Name:", self.store_name)
        print("Total Items:", len(self.inventory.products))
        print("Total Inventory Value: Rs.", self.inventory.get_total_value())
        print("=============================")


# testing the store system
s = Store("Electronics Corner")

# adding 3 products
print("Adding products to store...")
s.add_new_product("Laptop", 50000, "Electronics")
s.add_new_product("Headphones", 1500, "Accessories")
s.add_new_product("Smartwatch", 4000, "Wearables")

# showing inventory list
s.inventory.show_all_products()

# showing store summary
s.show_summary()

# testing operator overloading (__add__)
item1 = s.inventory.products[0]
item2 = s.inventory.products[1]
combined_total = item1 + item2

print("\nCombining price of Laptop and Headphones using '+' operator:")
print("Combined price: Rs.", combined_total)
