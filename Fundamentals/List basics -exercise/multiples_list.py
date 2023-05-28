factor = int(input())
count = int(input())

number_list = []

for multiplier in range(1, count + 1):
    number_list.append(factor * multiplier)

print(number_list)
