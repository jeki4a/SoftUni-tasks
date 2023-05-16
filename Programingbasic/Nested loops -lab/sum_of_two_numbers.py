first = int(input())
second = int(input())
magic_number = int(input())

combinations = 0

for i in range(first, second + 1):
    for j in range(first, second + 1):
        combinations += 1
        if i + j == magic_number:
            print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
            break
    else:
        continue
    break
else:
    print(f"{combinations} combinations - neither equals {magic_number}")
