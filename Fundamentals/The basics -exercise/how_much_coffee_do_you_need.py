coffees = 0

while True:
    command = input()
    if command == "END":
        break
    elif command.isupper():
        if command == "DOG" or command == "CAT" or command == "CODING" or command == "MOVIE":
            coffees += 2
    elif command == "dog" or command == "cat" or command == "coding" or command == "movie":
        coffees += 1
    else:
        continue

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
