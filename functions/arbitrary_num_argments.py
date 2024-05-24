# Arbitrary Number of Arguments

'''
Question: How many arguments can a function accept?

Answer: Sometimes you don't know in advance how many arguments a function will accept.


So how do you solve this problem?

Well, in Python, you can pass an arbitrary number of arguments to your function by adding an asterisk (*)
to the front of a parameter name, like so:

def make_pizza(*toppings):
    """Print the list of toppings the customer requested."""
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('hamburger')
print()
make_pizza('mushrooms', 'green peppers', 'pepperoni')

'''

# In the first function call, we used just one argument (hamburger)
# But in the second function call, we passed three arguments -- mushrooms, green peppers, and pepperoni -- to the parameter list
# Because we added a * to the front of the parameter toppings, we can pass any number of arguments to the function,
# and Python will run the function without complaining

# Your assignment:

# First, complete the Try It Yourself activity on page 150 in Python Crash Course, 8-12 (Sandwiches)

# Next, write your own function that will accept any number of arguments; the function should describe 
# the traits (qualities or powers) of a game character

# Like the make_pizza example above, use a FOR loop to run through the list of traits and describe the 
# character from your game

def make_sandwiches(*ingredients):
    '''A function that displays the ingredients a customer wants on their sandwich.'''
    print('You requested these ingredients on your sandwich:')
    for ingredient in ingredients:
        print(f'- {ingredient}')
    print()
make_sandwiches('Swiss cheese', 'ham')
make_sandwiches('red onions')
make_sandwiches('mustard', 'pickles', 'tomatoes', 'diced onions', 'olive oil')

def describe_character(*traits):
    '''A function that lists the traits of a game character.'''
    print('List of the traits of your game character:')
    for trait in traits:
        print(f' > {trait}')
    print()

describe_character('Can shape shift')
describe_character('Can go invisible', 'bulletproof')
describe_character('Has super speed', 'stealth mode', 'super strength', 'unlimited endurance')