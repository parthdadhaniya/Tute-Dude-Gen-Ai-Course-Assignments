# Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

# Write sales data line by line
file = open("sales_data.txt", "w")
for sale in sales:
    file.write(str(sale) + "\n")
file.close()

# Optional Task 1: Write sales data in comma-separated format
csv_file = open("sales_data_csv.txt", "w")
csv_file.write(", ".join(str(s) for s in sales) + "\n")
csv_file.close()

print("Sales data written to sales_data.txt")
print("Comma-separated sales written to sales_data_csv.txt\n")

# Read and print contents
print("Contents of sales_data.txt:")
file = open("sales_data.txt", "r")
print(file.read())
file.close()

