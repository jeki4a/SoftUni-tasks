sheep = input().split()

count = 0
for animal in sheep:
    if animal != "wolf":
        count += 1

if sheep.pop() == "wolf":
    print("Please go away and stop eating my sheep")
else:
    count += 1
    print("Oi! Sheep number", count, "! You are about to be eaten by a wolf!")