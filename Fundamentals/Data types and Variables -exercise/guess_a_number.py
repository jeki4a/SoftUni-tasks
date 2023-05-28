import random

pc_number = random.randint(1, 100)

number_unknown = True

while number_unknown:
    guess = int(input())
    if guess > 100 or guess < 1:
        print("Please pick a number between 1 and 100")
        pass
    elif guess < pc_number:
        print("Too low")
        pass
    elif guess > pc_number:
        print("Too high")
        pass
    else:
        print(f"You guessed the number! \nThe number was: {pc_number}")
        break
