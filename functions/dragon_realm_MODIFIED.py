#################################################
# Name: Bruce Provencher
# Project: Dragon Realm MODIFIED
# Date: 20 OCT 2014 
#################################################

import random
import time

def displayIntro():
    print('You are on a planet full of dragons. In front of you, you see two caves.')
    time.sleep(2)
    print('In one cave, the dragon is friendly and will share his treasure with you.')
    time.sleep(2)
    print('The other dragon is greedy and hungry, and will eat you on sight!')
    time.sleep(2)
   
def chooseCave():
    cave = ''
    caveList = [1,2]
    while cave not in caveList:
        print('Which cave do you wish to enter?(1 or 2)')
        cave = int(input())

    return cave

def checkCave(chosenCave):

    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('You notice a huge shadow looming over you...')
    time.sleep(3)
    print('A large dragon appears in front of you! He opens his jaws and...')
    time.sleep(4)
    print()

    randCave = random.randint(1,3)
    # This portion of the project has been modified from the original
    if randCave == 1:
        print('The dragon greets you and gives you his treasure!')
    elif randCave == 2:
        print('The dragon crushes you with it\'s powerful jaws and eats you!')
    else:
        print('You realize the cave is empty. Your mind must be playing tricks on you ...')
   
playAgain = 'yes'
while playAgain.lower() == 'yes' or playAgain.lower() == 'y':
    print()
    displayIntro()

    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (y/n)')
    playAgain = input()
