n1 = int(input())
n2 = int(input())
operator = input()

if operator == "+":
    result = n1 + n2
    even_odd = "even" if result % 2 == 0 else "odd"
    print(f"{n1} + {n2} = {result} - {even_odd}")
elif operator == "-":
    result = n1 - n2
    even_odd = "even" if result % 2 == 0 else "odd"
    print(f"{n1} - {n2} = {result} - {even_odd}")
elif operator == "*":
    result = n1 * n2
    even_odd = "even" if result % 2 == 0 else "odd"
    print(f"{n1} * {n2} = {result} - {even_odd}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        remainder = n1 % n2
        print(f"{n1} % {n2} = {remainder}")
else:
    print("Invalid operator")
