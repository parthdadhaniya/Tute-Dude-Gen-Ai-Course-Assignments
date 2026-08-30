# Task 4: Loop Control with Conditions (break & continue)
# Process daily sales, skipping 0 (no sales) and stopping at -1 (corrupted data)

daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

print("Processing Daily Sales:")
print("----------------------------------------")

for sale in daily:
    if sale == -1:
        print("Corrupted data (-1) encountered! Stopping loop.")
        break
    
    if sale == 0:
        print("No sales today (0). Skipping...")
        continue
    
    total_sales += sale
    print(f"Added sale: ${sale} | Total Sales: ${total_sales}")

print("----------------------------------------")
print(f"Final Total Sales: ${total_sales}")
