# Task 2: Read File in Different Ways

print("--- Method 1: Using read() ---")
file = open("sales_data.txt", "r")
content = file.read()
print(content)
file.close()

print("--- Method 2: Using readline() ---")
file = open("sales_data.txt", "r")
first_line = file.readline()
print("First line:", first_line.strip())
file.close()

print("--- Method 3: Using readlines() ---")
file = open("sales_data.txt", "r")
lines = file.readlines()
file.close()

sales_numbers = []
for line in lines:
    if line.strip():
        sales_numbers.append(int(line.strip()))

print("Sales list as integers:", sales_numbers)

