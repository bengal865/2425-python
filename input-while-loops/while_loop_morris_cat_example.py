# WHILE Loop / Modifying A Python List

# Create my Python list of pets
pets = ['hamster', 'cat', 'python', 'goldfish', 'ferret', 'rabbit', 'cat']

print("Here is your original list of pets:")
print(pets)

# What do lines 10 and 12 do?
while 'cat' in pets:

    pets.remove('cat')

# Print the modified lists of pets
print("\n\nYour updated list of pets:")
print(pets)
