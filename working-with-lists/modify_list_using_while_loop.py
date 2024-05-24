# Programmer: Bruce Provencher
# Date: 24 OCT 2018
# WHILE Loop / Modifying A Python List

# Create my Python list of pets
pets = ['hamster', 'cat', 'python', 'goldfish', 'ferret', 'rabbit', 'cat']
# Display the original list of pets
print("Here is your original list of pets:")
print(pets)

# Use WHILE loop to move through the list (from
# beginning to end)
# Python is searching for the word 'cat' in my list of pets
while 'cat' in pets:
	# Remove any instance of the word 'cat' from the list...
    pets.remove('cat')

# Print the modified lists of pets
print("\n\n\nAnd here is the modified list of pets (minus the cats):")
print(pets)