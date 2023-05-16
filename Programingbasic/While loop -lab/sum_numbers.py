n = int(input())

sum = 0

while sum <= n:
    numbers = int(input())
    sum += numbers
    if sum >= n:
        break

print(sum)