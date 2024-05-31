# Mike Jenkins
# 17 JAN 20XX
# Space Adventure Game

import random
import time

def displayIntro():
    print("It is the end of a long year of fighting space criminals.")
    print("You come to crossroads on your trip home -- one path leads home,")
    print("where you will be handsomly rewarded for a job well done, ")
    print("and the other leads through a gamma ray burst that will destroy you.")
    print()

def choosePath():
    path = "" # Set path variable equal to an empty string
    while path != "1" and path != "2": # Input validation
        path = input("Which path will you choose? (1 or 2):\n")
    return path

def checkPath(chosenPath):
    print("You head down the path...")
    time.sleep(2)
    print("and notice a nearby asteroid that looks vaguely familiar...That must be a good sign...")
    time.sleep(2)
    print("but your skin begins to tingle...")
    print()
    time.sleep(2)


    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That tingling sensation was just you sensing the love")
        print("and admiration the citizens of the galaxy have for you!")
        print("Welcome home, destroyer of space criminals!")
    else:
        print("A monumental burst of gamma rays rips through you,")
        print("causing all of the atoms in your body to dissociate!")
        print("Before you realize it, you've been vaporized, and no trace of your existence remains!")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # Is choice equal to "1" or "2"?
    playAgain = input("Do you want to play again? (Enter 'yes, or 'y' to continue playing): ")