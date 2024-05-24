# Programmer:
# Date: 08 FEB 2017
# Project: Number Guess Game

import random

def is_valid_num(s):
    if s.isdigit() and int (s) >= 1 and int(s) <= 100:
        return True
    else:
        return False

def main ():

    number = random.randint(1,100)
    guessed_number = False
    guess = input ("Guess a number between 1 and 100:\n")
    num_guesses = 0

    while not guessed_number:
        if not is_valid_num(guess):
            guess = input ("I won't count that one! Please enter a number from 1 to 100...\n")
            continue
        else:
            num_guesses += 1
            guess = int (guess)

        if guess < number:
            guess = input ("Too low! Guess again!\n")
        elif guess > number:
            guess = input ("Whoa! Too high! Guess again!\n")
        else:
            print ("You guessed the number in",num_guesses,"guesses!")
            guessed_number = True

    print ("\n\nThanks for playing my Number Guess game.")

main()
