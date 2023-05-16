budget = int(input())

while True:
    price = input()
    if price == "End":
        break
    else:
        price = int(price)
        budget -= price
        if budget < 0:
            break
if budget < 0:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
