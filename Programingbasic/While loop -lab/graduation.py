name = input()
grades = 0
years = 0
failed = 0

while True:
    grade = float(input())

    if grade < 4:
        failed += 1

        if failed == 2:
            failed_year = years + 1
            print(f"{name} has been excluded at {failed_year} grade")
            break
    else:
        years += 1
        grades += grade
        avg_grade = grades / years
    if years == 12:
        print(f"{name} graduated. Average grade: {avg_grade:.2f}")
        break