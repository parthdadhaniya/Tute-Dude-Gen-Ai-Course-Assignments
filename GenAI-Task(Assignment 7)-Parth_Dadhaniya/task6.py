# Task 6 - Magic Methods and Operator Overloading

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # string representation magic method
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # overloading + operator
    def __add__(self, other):
        return self.price + other.price


# testing magic methods
prod1 = Product("Keyboard", 1200, "Accessories")
prod2 = Product("Mouse", 800, "Accessories")

# testing __str__
print("Product 1:", prod1)
print("Product 2:", prod2)

# testing __add__
total = prod1 + prod2
print("Total price of both products:", total)
