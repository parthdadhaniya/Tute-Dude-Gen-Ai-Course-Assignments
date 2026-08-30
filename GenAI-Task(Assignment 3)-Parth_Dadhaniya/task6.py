# Task 6 - Combined Utility Function

def process_prices(prices):
    # 10% discount using map and lambda
    discounted_prices = list(map(lambda price: price * 0.9, prices))
    # Filter prices > 300 using filter and lambda
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))
    return discounted_prices, filtered_prices

if __name__ == "__main__":
    print("--- Task 6: Combined Utility Function ---")
    input_prices = [500, 900, 50, 750]
    
    disc_prices, filt_prices = process_prices(input_prices)
    
    print("Input Prices:             ", input_prices)
    print("Discounted Prices (10% off):", disc_prices)
    print("Filtered Prices (> 300):    ", filt_prices)

