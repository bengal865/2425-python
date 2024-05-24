###############################
#Programmer: Alyssa Tarkowski
#Date: 7 November 2018
#Project: Mad Libs
###############################

import random, time

# Assign lists
player = ["LeBron James", "Miguel Cabrera", "Del Curry", "George Washington"]
sport = ["basketball", "baseball", "football", "lacrosse"]
team = ["Los Angeles Lakers", "Detroit Lions", "Boston Red Socks", "Cleveland Cavaliers"]
past_particle = ["broke", "injured", "sprained", "damaged"]
body_part = ["nose", "knee", "back", "ankle"]
verb = ["running", "shooting", "standing", "sitting on the bench"]
number1 = [3, 103, 45, 7]
number2 = [2, 5, 99, 32]
team2 = ["Texas Rangers", "Golden State Warriors", "Boston Celtics", "Chicago Cubs"]

# Intro/welcomes user
name = input("Please enter your first name:\n")
time.sleep(1)
print()
print (f"Hello {name.title()}! Welcome to my Mad Lib Game!")
time.sleep(.75)

input("To view your randomly gernerated mad lib, press ENTER")
print()
print("Generating your mad lib...")
time.sleep(1.5)

# Generates mad lib story
print(f'''
BREAKING NEWS: {player[random.randint(0,3)]}, who plays {sport[random.randint(0,3)]} for the {team[random.randint(0,3)]}, was injured at the game last night.
Officials say he had {past_particle[random.randint(0,3)]} his {body_part[random.randint(0,3)]} while {verb[random.randint(0,3)]}.
It is predicted that he will not be able to play for {number1[random.randint(0,3)]} games, and will have to do rehab for {number2[random.randint(0,3)]} weeks.
His team will be at a loss without him when they play the {team2[random.randint(0,3)]} tomorrow night. 

''')
