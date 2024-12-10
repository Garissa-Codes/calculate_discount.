def calculate_discount(price, discount_percent):

# Checking if the discount percentage meets or exceeds the threshold of 20%
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Getting user input
try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

# Calculating and print the final price
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError as e:
    if 'could not convert string to float' in str(e):
        print("Invalid input. Please ensure you enter numeric values for both price and discount percentage.")
    else:
        print("An unexpected error occurred. Please try again.")
