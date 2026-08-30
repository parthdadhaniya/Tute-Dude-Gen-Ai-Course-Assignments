# Task 5 - Using filter(): Filter Expensive Products

# Given list of prices
prices = [100, 250, 400, 1200, 50, 2000, 850]

# Use filter() to keep prices greater than 500
expensive_prices = list(filter(lambda price: price > 500, prices))

# Use filter() to keep prices less than or equal to 500
affordable_prices = list(filter(lambda price: price <= 500, prices))

# Output results
if __name__ == "__main__":
    print("--- Task 5: Filter Prices ---")
    print("Original prices:           ", prices)
    print("Prices > 500 (Expensive):  ", expensive_prices)
    print("Prices <= 500 (Affordable):", affordable_prices)
