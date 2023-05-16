budget = float(input())
num_extras = int(input())
price_per_extra = float(input())

set_cost = budget * 0.1
clothing_cost = num_extras * price_per_extra

if num_extras > 150:
    clothing_cost *= 0.9

total_cost = set_cost + clothing_cost

if total_cost > budget:
    money_short = total_cost - budget
    print(f"Not enough money!\nWingard needs {money_short:.2f} leva more.")
else:
    remaining_money = budget - total_cost
    print(f"Action!\nWingard starts filming with {remaining_money:.2f} leva left.")
