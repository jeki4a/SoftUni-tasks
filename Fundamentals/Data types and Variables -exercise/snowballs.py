from sys import maxsize

snowballs_count = int(input())

max_value = float(-maxsize)
best_snowball = ''

for _ in range(snowballs_count):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > max_value:
        max_value = snowball_value
        best_snowball = f"{snowball_weight} : {snowball_time} = {snowball_value:.0f} ({snowball_quality})"

print(best_snowball)
