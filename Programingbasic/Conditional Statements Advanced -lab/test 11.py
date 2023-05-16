fruit = input()
day_of_the_week = input()
quantity = float(input())

if (fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes") and (day_of_the_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]):
    try:

        price = 0

        if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Thursday" or day_of_the_week == "Wednesday" or day_of_the_week == "Friday":
            if fruit == "banana":
                price = 2.50
            elif fruit == "apple":
                price = 1.20
            elif fruit == "orange":
                price = 0.85
            elif fruit == "grapefruit":
                price = 1.45
            elif fruit == "kiwi":
                price = 2.70
            elif fruit == "pineapple":
                price = 5.50
            elif fruit == "grapes":
                price = 3.85

        elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
            if fruit == "banana":
                price = 2.70
            elif fruit == "apple":
                price = 1.25
            elif fruit == "orange":
                price = 0.90
            elif fruit == "grapefruit":
                price = 1.60
            elif fruit == "kiwi":
                price = 3.00
            elif fruit == "pineapple":
                price = 5.60
            elif fruit == "grapes":
                price = 4.20

        final_price = quantity * price

        print(f"{final_price:.2f}")

    except ValueError:
        print("error")

else:
    print("error")
