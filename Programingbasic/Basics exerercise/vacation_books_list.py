number_of_pages = int(input())
reading_speed = int(input())
days = int (input())

time_needed = number_of_pages // reading_speed

time_needed_in_days = time_needed // days

print(time_needed_in_days)
