numbers = list(map(int, input().split()))
n = int(input())

numbers = sorted(numbers)[n:]

print(", ".join(map(str, numbers)))
