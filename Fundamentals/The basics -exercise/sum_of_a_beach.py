s = input().lower()
count_sand = s.count("sand")
count_water = s.count("water")
count_fish = s.count("fish")
count_sun = s.count("sun")
total = count_sand + count_water + count_fish + count_sun
print(total)
