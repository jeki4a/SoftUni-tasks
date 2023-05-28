numbers = [ 1, 5, 6, 7]

num_1 = 0
num_2 = 0

for num in numbers:
    if num > 5:
        num_1 = num
    else:
        num_2 = num

result = num_1 - num_2
print(result)