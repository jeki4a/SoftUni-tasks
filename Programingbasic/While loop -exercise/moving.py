width = int(input())
length = int(input())
height = int(input())

boxes = 0

space = width * length * height

while space > boxes:
    command = input()
    if command == 'Done':
        break
    boxes += int(command)

diff = space - boxes

if diff > 0:
    print(f"{diff} Cubic meters left.")
else:
    diff = abs(diff)
    print(f"No more free space! You need {diff} Cubic meters more.")
