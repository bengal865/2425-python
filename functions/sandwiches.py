# Working with arguments
def sandwich_toppings(*toppings):
    '''Function that lists the toppings the customer wants on their sandwich.'''
    print(f'\nMaking a sandwich with these toppings on it:')
    for topping in toppings:
        print(f'- {topping}')


sandwich_toppings('lettuce')
sandwich_toppings('hot peppers', 'bologna', 'Swiss cheese')
sandwich_toppings('horseradish', 'onions',
                  'spicy barbecue sauce', 'green onions')
