#############################################
# Author: Bruce Provencher
# Project: DRAGON REALM / SWEIGART TEXTBOOK
# Date: 29 MAY 2020
#############################################

import random, time

# Function for displaying the game introduction
def displayIntro():
	print ("You are in a land full of dragons.  Before you lie")
	print ("two caves.  In one cave, the dragon is known to be friendly, ")
	print ("and will share his treasure with you.")
	print()
	print("The dragon in the other cave, however, is greedy and hungry,")
	print ("and will, without hesitation, devour you on sight.  Be warned!")
	print()
	
def chooseCave():
	cave = ""
	while cave != '1' and cave != '2':
		print ("Which cave do you wish to enter? (1 or 2)")
		cave = input()
		
	return cave

def checkCave(caveChosen):
	print("And so you approach the cave...")
	time.sleep(2)
	print("It's dark and spooky...")
	time.sleep(2)
	print("A gigantic dragon suddenly launches himself out of the cave! He opens his jaws and...")
	print()
	time.sleep(2)
	
	friendlyCave = random.randint(1,2)
	
	if caveChosen == str(friendlyCave):
		print("...gives you his treasure!")
	else:
		print("...gobbles you down in one bite!")
		
playAgain = "yes"

while playAgain == "yes" or playAgain == "y":

	time.sleep(2)

	displayIntro()
	
	time.sleep(2)
	
	caveNumber = chooseCave()
	
	time.sleep(2)
	
	checkCave(caveNumber)
	
	print("Do you want to play again (y/n)")
	playAgain = input()
	playAgain = playAgain.lower()
	

