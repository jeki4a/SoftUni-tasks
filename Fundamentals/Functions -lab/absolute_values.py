numbers = input().split()

abs_numbers = []

for num in numbers:
    num = float(num)
    abs_numbers.append(abs(num))


print(abs_numbers)
