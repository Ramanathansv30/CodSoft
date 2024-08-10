import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie game!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You have won the game :)")
    else:
        print("You have lost the game :(")

    if input("Do you want to continue the game (Y/N): ").lower() != "y":
        running = False

print("THE Game is Over")