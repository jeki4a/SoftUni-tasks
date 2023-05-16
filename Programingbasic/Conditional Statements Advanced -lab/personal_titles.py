age = float(input())
sex = str(input())

if sex == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

else:
 if age >= 16:
        print("Mr.")
 else:
     print("Master")
