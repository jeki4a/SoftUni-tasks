steps = 0
goal = 10000

while steps < goal:
    command = input()
    if command == 'Going home':
        steps_home = int(input())
        steps += steps_home
        break
    steps += int(command)

diff = abs(steps - goal)

if steps >= goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
