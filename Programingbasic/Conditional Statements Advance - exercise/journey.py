budget = float(input())
season = input()

destination = ""
vacation_type = ""
amount_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        amount_spent = 0.3 * budget
    elif season == "winter":
        vacation_type = "Hotel"
        amount_spent = 0.7 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        amount_spent = 0.4 * budget
    elif season == "winter":
        vacation_type = "Hotel"
        amount_spent = 0.8 * budget
else:
    destination = "Europe"
    vacation_type = "Hotel"
    amount_spent = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {amount_spent:.2f}")
