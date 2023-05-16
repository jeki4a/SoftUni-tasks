while True:
    name = input()
    chars = len(name)
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        exit()
    elif name == "Voldemort":
        print("You must not speak of that name!")
        exit()
    elif chars < 5:
        print(f"{name} goes to Gryffindor.")
    elif chars == 5:
        print(f"{name} goes to Slytherin.")
    elif chars == 6:
        print(f"{name} goes to Ravenclaw.")
    elif chars > 6:
        print(f"{name} goes to Hufflepuff.")
