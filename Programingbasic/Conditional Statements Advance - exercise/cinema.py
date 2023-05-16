type_of_projection = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if type_of_projection == "Premiere":
    income = cinema_capacity * 12.00
elif type_of_projection == "Normal":
    income = cinema_capacity * 7.50
elif type_of_projection == "Discount":
    income = cinema_capacity * 5.00

print(f'{income:.2f} leva')

