#Project number 4. related with a bootcamp.
#Made by Piotr Zięba on 17.10.2023.
#It is a game: rock, scissors, paper. The computer uses random numbers to play.

import random #imported module
x = True #default x
while x: #it makes the game start again
    user_choice = int(input("Choose 0 for scissors, 1 for rock and 2 for paper:")) #

    if user_choice == 0: # player's choice.
        print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    SCISSORS
    """)
    elif user_choice == 1:
        print(""" 
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ROCK
    """)
    elif user_choice == 2:
        print("""
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    PAPER
    """)


    number = random.randint(0, 2) # random choice for the computer from 0 to 2.
    if number == 0:
        print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    SCISSORS
    """)
    elif number == 1:
        print(""" 
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ROCK
    """)
    elif number == 2:
        print("""
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    PAPER
    """)
#bellow are the game results.
    if (user_choice == 0 and number == 2) or (user_choice == 1 and number == 0) or (user_choice == 2 and number == 1):
        print("You win!")
    elif (user_choice == 2 and number == 0) or (user_choice == 0 and number == 1) or (user_choice == 1 and number == 2):
        print("You lose!")
    else:
        print("It's a draw!")
#It allows the player to choose whether to start again or not.
    x = input("Do you want to play again? Y or N").lower()
    if x == "y":
        x = True
    elif x == "n":
        x = False
    else:
        print("Sorry, wrong answer. I will take that as a yes.")
        x = True