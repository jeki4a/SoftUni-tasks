string = input()

capitals = []

for i in range(len(string)):
    if string[i].isupper():
        capitals.append(i)

print(capitals)
