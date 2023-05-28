list_numbers = input().split()

new_list = []

for numbers in list_numbers:
    number = int(numbers)
    if number < 0:
        number *= -1
    else:
        number *= -1
    new_list.append(number)



print(new_list)
