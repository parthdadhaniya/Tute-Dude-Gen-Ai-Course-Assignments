# Task 1 - Basic class and object creation

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # method to show product info
    def get_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print("--------------------")

    # extra method to apply discount
    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        return self.price - discount


# creating two product objects
p1 = Product("Laptop", 55000, "Electronics")
p2 = Product("Headphones", 2000, "Accessories")

# calling get_info method
print("Product 1 Info:")
p1.get_info()

print("Product 2 Info:")
p2.get_info()

# testing discount method
disc_price = p1.apply_discount(10)
print("Price of Laptop after 10% discount:", disc_price)
