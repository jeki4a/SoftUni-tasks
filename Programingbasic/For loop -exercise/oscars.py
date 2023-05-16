actor = input()
starting_points = float(input())
evaluators = int(input())

for i in range(evaluators):
    name = input()
    points = float(input())
    starting_points += (len(name) * points) / 2
    if starting_points > 1250.5:

        break

if starting_points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {starting_points:.1f}!")
else:
    needed_points = 1250.5 - starting_points
    print(f"Sorry, {actor} you need {needed_points:.1f} more!")
