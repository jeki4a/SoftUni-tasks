import sys

biggest_number = sys.maxsize

while True:
    n = input()
    if n == "Stop":
        print(biggest_number)
        break
    else:
        n = int(n)
        if n < biggest_number:
            biggest_number = n


