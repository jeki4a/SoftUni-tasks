total = 0

while True:
    n = input()
    if n == "NoMoreMoney":
        break
    n = float(n)
    if n < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {n:.2f}")
    total += n

print(f"Total: {total:.2f}")
