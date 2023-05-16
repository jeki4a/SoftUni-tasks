tournaments = int(input())
points = int(input())

t_points = 0
w = 0

for _ in range(tournaments):
    stage = input()
    if stage == "W":
        t_points += 2000
        w += 1
    elif stage == "F":
        t_points += 1200
    elif stage == "SF":
        t_points += 720

points += t_points

print(f"Final points: {points}")
print(f"Average points: {t_points // tournaments}")
print(f"{(w / tournaments) * 100:.2f}%")
