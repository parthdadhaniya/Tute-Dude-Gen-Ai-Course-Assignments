# Task 5 - Abstraction using Abstract Base Class

from abc import ABC, abstractmethod

# Abstract base class
class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# CreditCard subclass
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Paid Rs.", amount, "using Credit Card.")


# UPI subclass
class UPIPayment(Payment):
    def process_payment(self, amount):
        print("Paid Rs.", amount, "using UPI.")


# testing abstract classes
p1 = CreditCardPayment()
p2 = UPIPayment()

p1.process_payment(2500)
p2.process_payment(500)
