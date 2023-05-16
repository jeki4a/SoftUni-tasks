city = input()
sales = float(input())

commission = 0

if sales < 0:
    print("error")
else:
    if city == "Sofia":
        if sales <= 500:
            commission = 0.05 * sales
        elif sales <= 1000:
            commission = 0.07 * sales
        elif sales <= 10000:
            commission = 0.08 * sales
        else:
            commission = 0.12 * sales
    elif city == "Varna":
        if sales <= 500:
            commission = 0.045 * sales
        elif sales <= 1000:
            commission = 0.075 * sales
        elif sales <= 10000:
            commission = 0.1 * sales
        else:
            commission = 0.13 * sales
    elif city == "Plovdiv":
        if sales <= 500:
            commission = 0.055 * sales
        elif sales <= 1000:
            commission = 0.08 * sales
        elif sales <= 10000:
            commission = 0.12 * sales
        else:
            commission = 0.145 * sales
    else:
        print("error")
        exit()

    print(f"{commission:.2f}")
