lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

cost = 0
broken_shield = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        cost += helmet_price
        if i % 3 == 0:
            cost += sword_price
            cost += shield_price
            broken_shield += 1
            if broken_shield >= 2:
                cost += armor_price
                broken_shield = 0
    elif i % 3 == 0:
        cost += sword_price

print(f"Gladiator expenses: {cost:.2f} aureus")