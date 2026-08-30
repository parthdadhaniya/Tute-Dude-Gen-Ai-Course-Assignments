# Assignment 7: Object Oriented Programming (OOP)

This project contains my Python code for Assignment 7 on Object-Oriented Programming (OOP). It covers basic OOP concepts like classes, encapsulation, inheritance, polymorphism, abstraction, magic methods, and a mini inventory system.

## Task Details

* **task1.py (Basic Class & Object Creation)**
  Creates a `Product` class with attributes `name`, `price`, `category`, a method `get_info()`, and a discount calculation method.

* **task2.py (Constructor & Encapsulation)**
  Makes the price attribute private (`__price`) and provides getter `get_price()` and setter `set_price()` with input validation.

* **task3.py (Inheritance)**
  Creates an `ElectronicProduct` subclass inheriting from `Product` with warranty details and method overriding.

* **task4.py (Polymorphism)**
  Creates `Laptop` and `Mobile` subclasses overriding `get_info()` and demonstrates polymorphism using a loop.

* **task5.py (Abstraction)**
  Creates an abstract class `Payment` with `@abstractmethod` and implements subclasses `CreditCardPayment` and `UPIPayment`.

* **task6.py (Magic Methods & Operator Overloading)**
  Implements `__str__` for string representation and `__add__` to combine prices using the `+` operator.

* **task7.py (Mini Project: Inventory System)**
  Combines `Product`, `Inventory`, and `Store` classes to add products, show summaries, calculate total value, and test operator overloading.

## How to Run

You can run each task individually from the terminal using Python 3:

```bash
python3 task1.py
python3 task2.py
python3 task3.py
python3 task4.py
python3 task5.py
python3 task6.py
python3 task7.py
```
