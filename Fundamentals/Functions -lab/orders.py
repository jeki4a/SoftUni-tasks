item = input()
amount = int(input())

def cost(item, amount):
    if item == "coffee":
        price = amount * 1.50
        return f"{price:.2f}"
    elif item == "water":
        price = amount * 1.00
        return f"{price:.2f}"
    elif item == "coke":
        price = amount * 1.40
        return f"{price:.2f}"
    elif item == "snacks":
        price = amount * 2.00
        return f"{price:.2f}"

print(cost(item, amount))