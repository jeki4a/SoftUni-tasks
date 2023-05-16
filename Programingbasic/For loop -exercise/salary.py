n = int(input())
salary = int(input())

fine = 0


for _ in range(n):
    site_name = input()
    if site_name == "Facebook":
        fine += 150
    if site_name == "Instagram":
        fine += 100
    if site_name == "Reddit":
        fine += 50

final_salary = salary - fine

if final_salary <= 0:
    print("You have lost your salary.")
else:
    print(final_salary)
