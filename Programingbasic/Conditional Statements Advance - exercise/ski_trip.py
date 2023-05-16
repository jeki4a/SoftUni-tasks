days_of_stay = int(input())
room_type = input()
evaluation = input()
nights = days_of_stay - 1

price = 0

if room_type == "room for one person":
    price = 18.00
elif room_type == "apartment":
    price = 25.00
    if days_of_stay < 10:
        price = price - (price * 0.3)
    elif days_of_stay <= 15:
        price = price - (price * 0.35)
    elif days_of_stay > 15:
        price = price - (price * 0.5)
elif room_type == "president apartment":
    price = 35.00
    if days_of_stay < 10:
        price = price - (price * 0.1)
    elif days_of_stay <= 15:
        price = price - (price * 0.15)
    elif days_of_stay > 15:
        price = price - (price * 0.2)

room_price = nights * price

if evaluation == "positive":
    room_price = room_price + (room_price * 0.25)
elif evaluation == "negative":
    room_price = room_price - (room_price * 0.1)

print(f"{room_price:.2f}")
