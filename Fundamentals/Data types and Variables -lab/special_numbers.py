n = int(input())

for i in range(1, n+1):
    digits = sum(int(digit) for digit in str(i))
    if digits == 5 or digits == 7 or digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
