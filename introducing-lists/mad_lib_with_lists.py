########################################
# Programmer: Bruce Provencher
# Date: 05 OCT 2018										
# Project: Mad Lib with Lists (Version 3.0)
########################################

import time, random
fname = ""

# Generate random integer between 0 and 3
# Use this number for the index number of 
# a list item
rand_index = random.randrange(0,4)

# Define the lists for this project
commands = ["run", "eat", "retreat", "swim"]
plural_nouns = ["boats", "clouds", "walls", "rocks"]
animals = ["tigers", "guinea pigs", "yaks", "leopards"]
locations = ["India", "Australia", "the grocery store", "the hardware store"]
singular_nouns = ["key", "spoon", "blender", "scarf"]
adjectives1 = ["smart", "spicy", "slippery", "obnoxious"]
adjectives2 = ["hungry", "tired", "hyper", "thoughtful"]
past_participles1 = ["run", "spoken", "eaten", "climbed"]
past_participles2 = ["questioned", "swiped", "flown", "navigated"]

# Create a variable to hold the finished story
story = """
{0}. But {1} only if ye be {2} of valor!
For {3} is guarded by a {4} so {5}, so {6},
that no {7} yet has {8} with it...and {9}!
""".format(commands[rand_index].title(), commands[rand_index], plural_nouns[rand_index], locations[rand_index], animals[rand_index], adjectives1[rand_index], adjectives2[rand_index], singular_nouns[rand_index], past_participles1[rand_index], past_participles2[rand_index])


fname = input("Please enter your first name:\n")
time.sleep(2)
print(f"""
Welcome to my Mad Lib Game, {fname}!
""")
time.sleep(2)
input("To view your randomly generated mad lib, press ENTER to continue...")
time.sleep(2)
print("Generating your mad lib...Please wait...")
time.sleep(4)
# Print the mad lib
print(story)


