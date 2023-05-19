n = int(input())

sum_ASCII = 0

for i in range(n):
    char = input()
    sum_ASCII += ord(char)

print(f"The sum equals: {sum_ASCII}")