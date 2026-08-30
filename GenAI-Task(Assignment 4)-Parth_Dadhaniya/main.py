# Assignment 4: Python File Handling - Main Runner
import os


def task1():
    print("=== Task 1: Write Sales Records ===")
    sales = [1200, 450, 980, 1500, 3000]

    # Write line by line
    file = open("sales_data.txt", "w")
    for sale in sales:
        file.write(str(sale) + "\n")
    file.close()

    # Optional Task 1: Comma-separated format
    csv_file = open("sales_data_csv.txt", "w")
    csv_file.write(", ".join(str(s) for s in sales) + "\n")
    csv_file.close()

    print("Sales data saved to sales_data.txt and sales_data_csv.txt.")

    print("\nContents of sales_data.txt:")
    file = open("sales_data.txt", "r")
    print(file.read())
    file.close()
    print()


def task2():
    print("=== Task 2: Read File in Different Ways ===")
    print("1. Using read():")
    file = open("sales_data.txt", "r")
    print(file.read())
    file.close()

    print("2. Using readline():")
    file = open("sales_data.txt", "r")
    line1 = file.readline()
    print("First line:", line1.strip())
    file.close()

    print("\n3. Using readlines():")
    file = open("sales_data.txt", "r")
    lines = file.readlines()
    file.close()

    sales_list = []
    for line in lines:
        if line.strip():
            sales_list.append(int(line.strip()))
    print("Sales list as integers:", sales_list)
    print()


def task3():
    print("=== Task 3: Append New Sales ===")
    new_sales = [5000, 2500, 1700]

    file = open("sales_data.txt", "a")
    for sale in new_sales:
        file.write(str(sale) + "\n")
    file.close()

    print("Appended new sales to sales_data.txt.")

    file = open("sales_data.txt", "r")
    lines = file.readlines()
    file.close()

    print("\nUpdated sales_data.txt contents:")
    for line in lines:
        print(line.strip())

    # Optional Task 3: Total number of lines
    print("\nTotal number of lines in file:", len(lines))
    print()


def task4():
    print("=== Task 4: Generate Summary Report ===")
    sales = []
    file = open("sales_data.txt", "r")
    for line in file:
        if line.strip():
            sales.append(int(line.strip()))
    file.close()

    total_sales = sum(sales)
    highest_sale = max(sales)
    lowest_sale = min(sales)
    average_sale = total_sales / len(sales)

    print("Total Sales:  ", total_sales)
    print("Highest Sale: ", highest_sale)
    print("Lowest Sale:  ", lowest_sale)
    print(f"Average Sale:  {average_sale:.2f}")
    print()


def task5():
    print("=== Task 5: Create Product Info File ===")
    products = []
    print("Enter details for 3 products:")
    for i in range(1, 4):
        name = input(f"Enter name for Product {i}: ")
        price = input(f"Enter price for Product {i}: ")
        products.append((name, price))

    file = open("products.txt", "w")
    for name, price in products:
        file.write(f"{name} | {price}\n")
    file.close()

    print("\nProduct details saved to products.txt.")

    print("\nContents of products.txt:")
    file = open("products.txt", "r")
    for line in file:
        print(line.strip())
    file.close()
    print()


def task6():
    print("=== Task 6: Read File Safely ===")
    filename = input("Enter filename to open: ")

    if os.path.exists(filename):
        print(f"\nOpening {filename}:")
        file = open(filename, "r")
        print(file.read())
        file.close()
    else:
        print("Error: File does not exist.")
    print()


def task7():
    print("=== Task 7: Export Discounted Prices ===")
    prices = {
        "Mouse": 500,
        "Keyboard": 800,
        "Monitor": 7000,
        "Pendrive": 400,
        "Camera": 5000
    }

    discount_pct = float(input("Enter discount percentage: "))

    discounted_prices = []

    file = open("discount_report.txt", "w")
    file.write("Product | Original Price | Discounted Price\n")
    file.write("-------------------------------------------\n")

    for product, orig_price in prices.items():
        disc_price = orig_price * (1 - discount_pct / 100)
        discounted_prices.append(disc_price)
        file.write(f"{product} | {orig_price} | {disc_price:.2f}\n")

    total_items = len(prices)
    avg_discounted_price = sum(discounted_prices) / total_items

    # Optional Task 7: Write summary block at bottom
    file.write("-------------------------------------------\n")
    file.write(f"Total Items: {total_items}\n")
    file.write(f"Average Discounted Price: {avg_discounted_price:.2f}\n")
    file.close()

    print("\nDiscount report saved to discount_report.txt.\n")

    print("--- Discount Report Contents ---")
    file = open("discount_report.txt", "r")
    print(file.read())
    file.close()
    print()


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()

