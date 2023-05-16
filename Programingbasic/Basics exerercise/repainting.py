plastic = int(input())
amount_of_paint = int(input())
paint_thinner = int(input())
hours_needed = int(input())

price_plastic = (plastic + 2) * 1.50
price_paint = (amount_of_paint * (10 / 100) + amount_of_paint ) * 14.50
price_thinner = paint_thinner * 5.00
price_bags = 0.40

products_price = price_bags + price_thinner + price_paint + price_plastic
workers_pay = (products_price * (30 / 100)) * hours_needed

final_price = products_price + workers_pay

print(final_price)










