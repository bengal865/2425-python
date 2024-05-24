# Programmer: Bruce Provencher
# Date: 01 NOV 2018
# Project: Mad Lib with List & Function

import time

# A global variable named 'story'
# As a global variable, ANY and ALL functions in the script
# can 'see' and access the variable 'story'
story = """
{}. But! {} only if ye be {} of valor!
For {} is guarded by a {} so {},
so {}, that no {} yet has {}
with it...and {}!
"""

def prompt_programmer():
	fname = input("Please enter your first name, programmer!\n")
	lname = input("And please enter your last name, programmer!\n")
	return [fname, lname]


def show_programmer_info(first_name, last_name):
	print(f"This program written by {first_name} {last_name} at")
	print("the TBAISD Career-Tech Center")
	print("Copyright 2018")

def main():
	

	# Introduce a delay of three seconds...
	time.sleep(3)
	# Get input from user
	command = input("Enter a command (Example: Eat):\n")
	plural_noun = input("Enter a plural noun (Example: dogs):\n")
	animal = input("Enter the name of an animal (Example: cow):\n")
	location = input("Enter a location (Example: Maine OR the store):\n")
	singular_noun = input("Enter a singular noun (Example: apple):\n")
	# Create an empty list called adjectives
	adjectives = []
	# Add adjectives to the list using the append () method
	adjectives.append(input("Enter an adjective (Example: spicy):\n"))
	adjectives.append(input("Enter another adjective:\n"))
	# Create an empty list called past participles
	past_participles = []
	# Add past participles to the list using the append () method
	past_participles.append(input("Enter a past participle (Example: played):\n"))
	past_participles.append(input("Enter another past participle:\n"))
	
	# Build the mad lib using the string format ( ) function
	mad_lib = story.format(command,
							command,
							plural_noun, 
							location, 
							animal,
							adjectives[0],
							adjectives[1],
							singular_noun,
							past_participles[0], 
							past_participles[1])
	# Print our mad lib						
	print(mad_lib)

# Call the function named show_programmer_info and pass to the function
# two arguments -- the first and last name of the programmer who wrote
# this script
my_returns = prompt_programmer()
show_programmer_info(my_returns[0], my_returns[1])

# Call the main function
main()