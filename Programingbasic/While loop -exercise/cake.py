width = int(input())
length = int(input())

pieces = width * length

while pieces > 0:
    command = input()
    if command == "STOP":
        break
    pieces -= int(command)

diff = abs(pieces)
if pieces > 0:
    print(f"{pieces} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")