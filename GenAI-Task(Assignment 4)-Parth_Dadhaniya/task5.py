# Task 5: Create Product Info File from User Input

products = []
print("Enter details for 3 products:")

for i in range(1, 4):
    name = input(f"Enter name for Product {i}: ")
    price = input(f"Enter price for Product {i}: ")
    products.append((name, price))

# Write to products.txt in format: ProductName | Price
file = open("products.txt", "w")
for name, price in products:
    file.write(f"{name} | {price}\n")
file.close()

print("\nProduct details saved to products.txt.")

# Read and print contents
print("\nContents of products.txt:")
file = open("products.txt", "r")
for line in file:
    print(line.strip())
file.close()

