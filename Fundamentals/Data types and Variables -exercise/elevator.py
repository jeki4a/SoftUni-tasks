capacity = int(input())
number_of_people = int(input())

courses = 0
if capacity <= number_of_people:
    print(1)
    exit()

while capacity > number_of_people:
    courses += 1
    capacity -= number_of_people


if capacity > 0:
    courses += 1
    print(courses)
else:
    print(courses)
