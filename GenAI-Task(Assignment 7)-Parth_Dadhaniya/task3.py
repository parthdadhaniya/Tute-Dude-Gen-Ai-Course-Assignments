# Task 3 - Single Level Inheritance

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


# Subclass inheriting from Product
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    # overriding get_info method
    def get_info(self):
        super().get_info()
        print("Warranty:", self.warranty_years, "Years")
        print("--------------------")


# testing inheritance
item = ElectronicProduct("Smart TV", 30000, "Electronics", 2)
item.get_info()
