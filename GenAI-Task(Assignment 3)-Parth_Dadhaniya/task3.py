# Task 3 - Lambda Function: GST Calculator

# Lambda function to calculate price after adding 18% GST
gst = lambda price: price + (0.18 * price)

# Extra (optional): Lambda to compute final price after applying discount first, then adding 18% GST
final_price_with_gst_and_discount = lambda price, discount_percent: (price * (1 - discount_percent / 100)) * 1.18

# Testing Task 3
if __name__ == "__main__":
    print("--- Task 3: GST Calculator ---")
    
    sample_price = 100
    price_with_gst = gst(sample_price)
    print(f"Original Price: {sample_price}")
    print(f"Price after 18% GST: {price_with_gst}")
    
    # Extra feature test
    discount_pct = 10
    final_amount = final_price_with_gst_and_discount(sample_price, discount_pct)
    print(f"\n[Extra] Price after {discount_pct}% discount + 18% GST: {final_amount:.2f}")
