# Task 4 - Using map(): Apply GST to List of Prices

# Define the GST lambda function (18% GST)
gst = lambda price: price + (0.18 * price)

# Given list of prices
prices = [100, 250, 400, 1200, 50]

# Use map() with the gst lambda to apply GST to each price in the list
prices_with_gst = list(map(gst, prices))

# Output results
if __name__ == "__main__":
    print("--- Task 4: Apply GST using map() ---")
    print("Original prices:   ", prices)
    print("Prices after GST:  ", prices_with_gst)
