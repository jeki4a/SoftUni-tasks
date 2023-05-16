type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if type_of_flower == "Roses":
    price = 5
    if number_of_flowers >= 80:
        price = price - (price * 0.1)
elif type_of_flower == "Dahlias":
    price = 3.80
    if number_of_flowers >= 90:
        price = price - (price * 0.15)
elif type_of_flower == "Tulips":
    price = 2.80
    if number_of_flowers >= 80:
        price = price - (price * 0.15)
elif type_of_flower == "Narcissus":
    price = 3
    if number_of_flowers <= 120:
        price = price + (price * 0.15)
elif type_of_flower == "Gladiolus":
    price = 2.50
    if number_of_flowers <= 80:
        price = price + (price * 0.2)

final_price = price * number_of_flowers


if budget >= final_price:
    remaining_money = budget - final_price
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {remaining_money:.2f} leva left.")

else:
    needed_money = final_price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
