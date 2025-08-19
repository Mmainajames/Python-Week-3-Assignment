def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount if discount is >= 20%.
    1st parameter is price: Original price of the item
    2nd parameter is discount_percent: Discount percentage
    If discount is less than 20%, the original price is returned.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

print(f"The final price is: {final_price:.2f}")


