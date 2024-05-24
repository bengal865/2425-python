# Arbitrary number of arguments to a function
def make_pizza(size, *toppings):
    '''Summarize the pizza we're about to make.'''
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')


make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'hamburger', 'sausage', 'extra cheese')
