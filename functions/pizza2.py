# Arbitrary number of arguments to a function
def make_pizza(*toppings):
    '''Summarize the pizza we're about to make.'''
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')


make_pizza('pepperoni')
make_pizza('mushrooms', 'hamburger', 'sausage', 'extra cheese')
