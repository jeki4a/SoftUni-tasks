budget = float(input())
price_flour = float(input())
eggs_price = price_flour * 0.75
milk_price = (price_flour + (price_flour * 0.25)) / 4
current_bread_count = 0
eggs_received = 0

total_price = price_flour + eggs_price + milk_price

while budget > total_price:
    current_bread_count += 1
    eggs_received += 3
    budget -= total_price
    if current_bread_count % 3 == 0:
        eggs_lost = current_bread_count - 2
        eggs_received -= eggs_lost

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {eggs_received} eggs and {budget:.2f}BGN left.")




