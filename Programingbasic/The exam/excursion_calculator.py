people = int(input())
season = input()

price = 0
price_per_person = 0

if season == "spring":
    if people <= 5:
        price_per_person = 50
    else:
        price_per_person = 48
elif season == "summer":
    if people <= 5:
        price_per_person = 48.50
    else:
        price_per_person = 45
    price_per_person *= 0.85
elif season == "autumn":
    if people <= 5:
        price_per_person = 60
    else:
        price_per_person = 49.50
elif season == "winter":
    if people <= 5:
        price_per_person = 86
    else:
        price_per_person = 85
    price_per_person *= 1.08

price = people * price_per_person

print(f"{price:.2f} leva.")
