name = input()
grades = 0
sum_grades = 0.0

while grades < 12:
    grade = float(input())
    if grade < 4.00:
        print(f"{name} has been excluded at {grades + 1} grade")
        break
    grades += 1
    sum_grades += grade
else:
    average_grade = sum_grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")

