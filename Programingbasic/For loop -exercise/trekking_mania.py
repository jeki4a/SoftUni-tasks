groups = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for _ in range(groups):
    people = int(input())
    if people <= 5:
        g1 += people
    if  people >= 6 and people <= 12:
        g2 += people
    if people >= 13 and people <= 25:
        g3 += people
    if people >= 26 and people <= 40:
        g4 += people
    if people >= 41:
        g5 += people

all_climbers = g1 + g2 + g3 + g4 + g5

g1_percent = (g1 / all_climbers) * 100
g2_percent = (g2 / all_climbers) * 100
g3_percent = (g3 / all_climbers) * 100
g4_percent = (g4 / all_climbers) * 100
g5_percent = (g5 / all_climbers) * 100

print(f"{g1_percent:.2f}%")
print(f"{g2_percent:.2f}%")
print(f"{g3_percent:.2f}%")
print(f"{g4_percent:.2f}%")
print(f"{g5_percent:.2f}%")
