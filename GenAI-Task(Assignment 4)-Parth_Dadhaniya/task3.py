# Task 3: Append New Sales Data

new_sales = [5000, 2500, 1700]

# Append new sales
file = open("sales_data.txt", "a")
for sale in new_sales:
    file.write(str(sale) + "\n")
file.close()

print("Appended new sales figures to sales_data.txt.\n")

# Read file and print contents along with total line count
file = open("sales_data.txt", "r")
lines = file.readlines()
file.close()

print("Updated sales_data.txt contents:")
for line in lines:
    print(line.strip())

print("\nTotal number of lines in file:", len(lines))

