import random

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors:")
    if player_move == "r":
        player_move = "rock"
        break
    elif player_move == "p":
        player_move = "paper"
        break
    elif player_move == "s":
        player_move = "scissors"
        break
    else:
        print("Invalid move")
        pass

moves = ["rock", "paper", "scissors"]

pc_move = random.choice(moves)

if (player_move == "rock" and pc_move == "scissors") or \
        (player_move == "paper" and pc_move == "rock") or \
        (player_move == "scissors" and pc_move == "paper"):
    print("You win!")
elif player_move == pc_move:
    print("Draw")
else:
    print("You lost.")
