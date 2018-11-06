# import the random package so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 5
computer_lives = 5


def winorlose(status):
    print("called win or lose function")
    print("*****")
    print("You", status, " ! Would you like to play again?")
    choice = input("Y / N: ")

    # reset the lives
    if choice == "Y" or choice == "y":
        # Chande global vaiables
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice == "n":
        print("You choose quit!")
        print("****")
        exit()


# make the computer choose a weapon from the choices array at random

computer_choice = choices[randint(0, 2)]

# show the computers choice in terminal window
print("computer chooses: ", computer_choice)

# set up our loop
while player is False:
    # set player to True by making a selection
    print("===========================")
    print("player_lives:", player_lives, "/5")
    print("computer_lives:", computer_lives, "/5")
    print("===========================")
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors")

    print(player, "\n")

    # check for a tie = choices are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")
    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            player_lives = player_lives = -1
            # computer won, crap!
            print("You lose! Paper covers Rock")
        else:
            computer_lives = computer_lives = -1
            # we win! such winning
            print("You win!", player, "smashes", computer_choice)

    elif player == "Paper":
        if computer_choice == "Scissors":
            player_lives = player_lives = -1
            print("You lose!", computer_choice, "cut", player)
        else:
            computer_lives = computer_lives = -1
            print("You win!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            player_lives = player_lives = -1
            print("You lose!", computer_choice, "smashes", player)
        else:
            computer_lives = computer_lives = -1
            print("You win!", player, "cuts", computer_choice)

    elif player == "quit":
        exit()
    else:
        print("Check your spelling... thats not a valid choice\n")

# Check win or lose
if player_lives is 0:
    print("You're out of lives! Would you like to play again?")

    choice = input("Y / N")

    if choice == "Y" or choice == "y":
        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]
    elif choice == "N" or choice == "n":
        print("You've had enough of losing")
        exit()

if computer_lives is 0:
    print("Computer is out of lives! Would you like to play again?")

    choice = input("Y / N")

    if choice == "Y" or choice == "y":
        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]
    elif choice == "N" or choice == "n":
        print("You've had enough of losing")
        exit()

    if player_lives is 0:
        winorlose("lose")

    if computer_lives is 0:
        winorlose("won")


# reset the game loop and start over
    player = False
    computer_choice = choices[randint(0, 2)]
