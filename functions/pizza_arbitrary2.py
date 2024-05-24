

# Example 1
def make_pizza(size, topping1, topping2):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    print(f"- {topping1}")
    print(f"- {topping2}")
        
make_pizza(12, 'pineapple', 'extra cheese')

# Example 2
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings: # Adds each topping to a TUPLE named toppings
        print(f"- {topping}")
       
make_pizza(12, 'sausage', 'black olives', 'extra cheese', 'pepperoni')
make_pizza(12, 'anchovies')

# Example 3
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

