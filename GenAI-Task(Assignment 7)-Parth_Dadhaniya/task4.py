# Task 4 - Polymorphism

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print("Product:", self.name, "| Price:", self.price)


# Laptop subclass
class Laptop(Product):
    def __init__(self, name, price, ram):
        super().__init__(name, price)
        self.ram = ram

    def get_info(self):
        print("Laptop:", self.name, "| RAM:", self.ram, "| Price: Rs.", self.price)


# Mobile subclass
class Mobile(Product):
    def __init__(self, name, price, storage):
        super().__init__(name, price)
        self.storage = storage

    def get_info(self):
        print("Mobile:", self.name, "| Storage:", self.storage, "| Price: Rs.", self.price)


# testing polymorphism with a list loop
l1 = Laptop("Dell Inspiron", 60000, "16GB")
m1 = Mobile("Redmi Note 12", 14000, "128GB")
l2 = Laptop("MacBook Air", 85000, "8GB")
m2 = Mobile("Samsung Galaxy M34", 18000, "128GB")

products = [l1, m1, l2, m2]

print("--- Product List Details ---")
for p in products:
    p.get_info()
