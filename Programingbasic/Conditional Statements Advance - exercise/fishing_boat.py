budget = int(input())
season = input()
num_fishermen = int(input())

price = 0

if season == "Spring":
    price = 3000
    if num_fishermen <= 6:
        price *= 0.9
    elif num_fishermen <= 11:
        price *= 0.85
    else:
        price *= 0.75
    if num_fishermen % 2 == 0:
        price *= 0.95
elif season == "Summer" or season == "Autumn":
    price = 4200
    if num_fishermen <= 6:
        price *= 0.9
    elif num_fishermen <= 11:
        price *= 0.85
    else:
        price *= 0.75
    if num_fishermen % 2 == 0 and season != "Autumn":
        price *= 0.95
elif season == "Winter":
    price = 2600
    if num_fishermen <= 6:
        price *= 0.9
    elif num_fishermen <= 11:
        price *= 0.85
    else:
        price *= 0.75
    if num_fishermen % 2 == 0:
        price *= 0.95

if budget >= price:
    remaining_money = budget - price
    print(f"Yes! You have {remaining_money:.2f} leva left.")
else:
    needed_money = price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
