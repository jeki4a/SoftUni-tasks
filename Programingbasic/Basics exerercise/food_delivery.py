chicken = int(input())
fish = int(input())
vegan = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.40
vegan_price = vegan * 8.15
dessert_price = (chicken_price + fish_price + vegan_price) * 20 / 100
desert_price_rounded = round(dessert_price, 2)
delivery_price = 2.50

final_price = chicken_price + fish_price + vegan_price + dessert_price + delivery_price
final_price_rounded = round(final_price , 2)
print(final_price_rounded)
