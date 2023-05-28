numbers = input().split()

rounded_numbers = []

def rounding(numbers, rounded_numbers):
    for num in numbers:
        num = round(float(num))
        rounded_numbers.append(num)
    return rounded_numbers

print(rounding(numbers, rounded_numbers))