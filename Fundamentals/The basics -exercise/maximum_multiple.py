from sys import maxsize

divisor = int(input())
boundary = int(input())

largest_num = -maxsize

for i in range(1, boundary + 1):
    if i % divisor == 0 and i <= boundary and i > 0:
        if i > largest_num:
            largest_num = i

print(largest_num)

