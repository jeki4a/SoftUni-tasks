needed_money = float(input())
cash_available = float(input())

days = 0
spend_days = 0

while True:
    action = input()
    amount = float(input())
    days += 1

    if action == "spend":
        spend_days += 1
        cash_available -= amount
        if cash_available < 0:
            cash_available = 0
    elif action == "save":
        cash_available += amount
        spend_days = 0
    if cash_available >= needed_money:
        print(f"You saved the money for {days} days.")
        break
    elif spend_days == 5:
        print("You can't save the money.")
        print(f"{days}")
        break
