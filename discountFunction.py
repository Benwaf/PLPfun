def calculate_discount(price, discount_percent):
    finalPrice = price - (price * discount_percent / 100)
    print(f"Price after discount: {finalPrice}")
    return finalPrice

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount on the original price: "))
calculate_discount(price, discount_percent)