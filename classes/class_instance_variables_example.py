# Class & Instance Variables Example
# 27 APR 2021
# Source: https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3

# Define our class -- the Shark class
class Shark():
    # animal_type is a CLASS variable (attribute)
    animal_type = 'fish'
    # Additional class variables (attributes)
    location = 'ocean'
    followers = 72

    # Unlike class variables, INSTANCE VARIABLES are defined within methods
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age

my_second_shark = Shark('Sammy', 6)
# Print some info about our second shark
print('Info about the second shark:')
print(f'First name: {my_second_shark.fname.title()}')
print(f'Age: {my_second_shark.age}')

stevie = Shark('Stevie', 8)
# Instance variables for Stevie
print(f'I know another shark named {stevie.fname}.')
print(f'{stevie.fname} is {stevie.age} years old.')
# Class variables for Stevie
print(f'Stevie is a {stevie.animal_type} who lives in the {stevie.location}.')




# Create an instance of the Shark class named new_shark
new_shark = Shark('Jaws', 4)
# Print the animal type using dot notation
print(new_shark.animal_type)
print(f'A shark is an example of a {new_shark.animal_type}.')

# Print more info about our new shark by accessing the other
# class variables
print(f'A shark lives in the {new_shark.location}.')
print(f'This shark has {new_shark.followers} followers on his Instagram account.')