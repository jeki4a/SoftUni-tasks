import sys

n = int(input())

max_num = -sys.maxsize
sum_numbers = 0

for _ in range(n):
    numbers = int(input())
    if numbers > max_num:
        max_num = numbers
    sum_numbers += numbers

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum= {max_num}")
else:
    print("No")
    sum_numbers = sum_numbers - max_num
    print(f"Diff= {abs(max_num - sum_numbers)}")
