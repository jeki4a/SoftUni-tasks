yard_square_meters = float(input())

price = yard_square_meters * 7.61
discount_price = price * (18/100)
final_price = (price - discount_price)

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_price} lv.")

