import random
restart = "y"
while restart == "y":
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissor?: ").lower()
    if player == computer:
        print("computer picked: " + computer)
        print("player picked: " + player)
        print("It's a tie")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "paper":
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "scissor":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("You lose!")
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("You win!")
    restart = input("Do you want do play again? Type Y and enter to play again. Hit Enter to exit ").lower()

print("Bye!")

