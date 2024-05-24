# Python Dictionary with WHILE Loop
# Source: https://www.youtube.com/watch?v=q8H5R6eP3zQ
# Net Ninja YT Tutorial

def ninja_intro(dictionary):
	for key, val in dictionary.items():
		print(f"I am {key} and I am a {val} belt ninja.")
	
ninja_belts = {} # Empty dictionary
while True:
	# ninja_name is the key
	ninja_name = input("Enter a name for your ninja:\n")
	# ninja_belt is the value
	ninja_belt = input("Please enter a belt color for your ninja:\n")
	ninja_belts[ninja_name] = ninja_belt
	
	another = input("Add another? (y/n)\n")
	if another.lower() == "y":
		continue
	else:
		break
		
# Call the function 'ninja_intro'
# Pass the dictionary 'ninja_belts' as an argument
ninja_intro(ninja_belts)