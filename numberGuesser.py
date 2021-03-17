#Nathan Li - Number Guessing Game - 1/29/2021

import random
num = random.randint(1,100)
play = "yes"

print("Welcome to the number guessing game!")
print("I will pick a random number between 1 and 100, and you will try to guess the number.")
while play == "yes":
    guess = int(input("Enter your guess between 1 and 100: "))
    points = 1
    while guess != num:
        if guess < num:
            print("That's too low!")
            points += 1
            guess = int(input("Try again: "))
        elif guess > num:
            print("That's too high!")
            points += 1
            guess = int(input("Try again: "))
    print("Congratulations, you took " + str(points) + " tries to guess my number!")

    """The following code propmts the user whether or not they would like to continue playing.
    Right now, it takes up a lot of space because it is done a crude way to keep asking until
    a desired input is read, yes or no. I may want to research more efficient ways of doing
    these loops"""
    play = str(input("Would you like to play again? Yes or no: "))
    if play.lower() == "yes":
        print("Awesome! Let's play the number guessing game.")
        num = random.randint(1,101)
    elif play.lower() == "no":
        print("Okay, have a nice day!")
        break
    else:
        print("Sorry, that's not a valid responce.")
        while play != "yes" and play != "no":
            play = str(input("Would you like to play again? Yes or no: "))
            if play.lower() == "yes":
                print("Awesome! Let's play the number guessing game.")
                num = random.randint(1,101)
            elif play.lower() == "no":
                print("Okay, have a nice day!")
                break
            else:
                print("Sorry, that's not a valid responce.")