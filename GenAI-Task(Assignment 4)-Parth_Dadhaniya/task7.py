# Task 7: Mini Project - Export Discounted Prices

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

# Optional Task 7: Write summary at bottom with Total Items and Average Discounted Price
file.write("-------------------------------------------\n")
file.write(f"Total Items: {total_items}\n")
file.write(f"Average Discounted Price: {avg_discounted_price:.2f}\n")
file.close()

print("\nDiscount report saved to discount_report.txt.\n")

print("--- Discount Report Contents ---")
file = open("discount_report.txt", "r")
print(file.read())
file.close()

