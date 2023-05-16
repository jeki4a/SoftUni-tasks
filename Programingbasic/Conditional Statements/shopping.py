budget = float(input())
num_gpus = int(input())
num_cpus = int(input())
num_ram = int (input())

price_gpus = num_gpus * 250
price_cpus = num_cpus * (0.35 * price_gpus)
price_ram = num_ram * (0.1 * price_gpus)

total_price = price_gpus + price_cpus + price_ram
if num_gpus > num_cpus:
    total_price = total_price - (total_price * 0.15)

if budget > total_price:
    remaining_money = budget - total_price
    print(f"You have {remaining_money:.2f} leva left")

else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
