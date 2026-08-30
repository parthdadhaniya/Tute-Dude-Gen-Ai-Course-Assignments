# Task 4: Generate Summary Report from File

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

print("--- Sales Summary Report ---")
print("Total Sales:  ", total_sales)
print("Highest Sale: ", highest_sale)
print("Lowest Sale:  ", lowest_sale)
print(f"Average Sale:  {average_sale:.2f}")

