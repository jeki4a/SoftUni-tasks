max_first = int(input())
max_second = int(input())
max_third = int(input())

for first in range(2, max_first + 1, 2):
    for second in [2, 3, 5, 7]:
        if second <= max_second:
            for third in range(2, max_third + 1, 2):
                print(f"{first} {second} {third}")
