# Task 7 - Mini Problem: Menu Using Functions

def add_price(prices_list, price):
    prices_list.append(price)
    print("Price added successfully!")

def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)

def main():
    prices = []
    
    while True:
        print("\n--- Price Management Menu ---")
        print("1. Add price")
        print("2. Show average price")
        print("3. Show highest price")
        print("4. Quit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            price = float(input("Enter price amount: "))
            add_price(prices, price)
        elif choice == '2':
            if len(prices) > 0:
                print("Current prices:", prices)
                print("Average price:", get_average_price(prices))
            else:
                print("No prices available to calculate average.")
        elif choice == '3':
            if len(prices) > 0:
                print("Current prices:", prices)
                print("Highest price:", get_max_price(prices))
            else:
                print("No prices available to find highest price.")
        elif choice == '4' or choice.lower() == 'q':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

