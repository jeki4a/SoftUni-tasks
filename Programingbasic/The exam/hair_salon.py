goal = int(input())

income = 0

while income < goal:
    command = input()
    if command == "closed":
        break
    elif command == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            income += 15
        elif haircut_type == "ladies":
            income += 20
        elif haircut_type == "kids":
            income += 10
    elif command == "color":
        color_type = input()
        if color_type == "touch up":
            income += 20
        elif color_type == "full color":
            income += 30

if income >= goal:
    print("You have reached your target for the day!")
    print(f"Earned money: {income}lv.")
else:
    print(f"Target not reached! You need {goal - income}lv. more.")
    print(f"Earned money: {income}lv.")

