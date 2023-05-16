excursion_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

toy_price = num_puzzles * 2.60 + num_dolls * 3 + num_bears * 4.10 + num_minions * 8.20 + num_trucks * 2

if num_puzzles + num_dolls + num_bears + num_minions + num_trucks >= 50:
    toy_price *= 0.75

final_price = toy_price * 0.9

if final_price >= excursion_price:
    remaining_money = final_price - excursion_price
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    money_needed = excursion_price - final_price
    print(f"Not enough money! {money_needed:.2f} lv needed.")
