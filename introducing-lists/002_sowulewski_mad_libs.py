################################
# Programmer: Elle Sowulewski
# Date: 9 NOV 2018
# Project: Mad Lib
################################

# Asks user for name

name = input("Please Enter Your Name: ")

# Imports modules

import time,random

# Makes lists

verbs = ['fly', 'swim', 'climb', 'caper']
singular_nouns = ['blanket', 'TV', 'flower', 'potato']
plural_nouns = ['donuts', 'rocks', 'kittens','shoes']
animals = ['dragon', 'fox', 'dog', 'chinchilla', 'cat', 'mouse', 'parakeet', 'unicorn', 'panda']
locations = ['the kitchen', 'the forest', 'Russia', 'Canada']
adjectives1 = ['cold', 'sleepy', 'sparkly', 'silly']
adjectives2 = ['clumsy', 'shiny', 'inspired', 'happy']
past_verb1 = ['tripped', 'fell', 'slept', 'laughed']
past_verb2 = ['shrugged', 'smiled', 'danced', 'yawned']

# Briefly explains before generating a story

print()
print(""" 			This program will generate a random story. 
			Press ENTER to generate your Mad Lib.
	""")
input()

time.sleep(1)

print("""			..... Generating your Mad Lib, please wait....
	""")
	
time.sleep(1)

# Story

rand1 = random.randrange(0,9)
print(f"			Once upon a time there was a {animals[rand1]} named {name}.")

rand2 = random.randrange(0,4)
print(f"			{name} could do many things. They could run, jump, or {verbs[rand2]}!")

rand3 = random.randrange(0,4)
print(f"			{name} was a little strange. They would sometimes get really {adjectives1[rand3]}.")

rand4 = random.randrange(0,4)
print(f"			One day, after getting {adjectives1[rand3]}, {name} took a {singular_nouns[rand4]}.")

rand5 = random.randrange(0,4)
print(f"			And, without rhyme or reason, they took the {singular_nouns[rand4]} into {locations[rand5]}.")

rand6 = random.randrange(0,4)
rand7 = random.randrange(0,4)
print(f"			After doing so, {name} {past_verb1[rand6]} on {plural_nouns[rand7]}.")

rand8 = random.randrange(0,4)
rand9 = random.randrange(0,4)
print(f"			{name} {past_verb2[rand8]} and continued on their day, feeling rather {adjectives2[rand9]}.")
print()
print("				The End!")



