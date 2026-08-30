# Task 2 - Constructor and Encapsulation

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price  # private attribute
        self.category = category

    # getter method for price
    def get_price(self):
        return self.__price

    # setter method for price with validation
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully!")
        else:
            print("Invalid price! Price should be greater than 0.")

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.get_price())
        print("Category:", self.category)
        print("--------------------")


# testing encapsulation
p = Product("Smartphone", 15000, "Electronics")
p.get_info()

# try setting invalid price
print("Setting price to -500:")
p.set_price(-500)

# setting valid price
print("\nSetting price to 18000:")
p.set_price(18000)

# final info
print("\nUpdated Product Details:")
p.get_info()
