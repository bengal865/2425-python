

# Example 1
# def make_pizza(size, topping1, topping2):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     print(f"- {topping1}")
#     print(f"- {topping2}")
        
# make_pizza(12, 'pineapple', 'extra cheese')
#make_pizza('pineapple', 12, 'extra cheese')
#make_pizza(topping2='pineapple', size=12, topping1='extra cheese')









# 1. Identify the PARAMETERS.
# 2. Where are the arguments?  What kind of arguments are they?



# Example 2 (creates tuple named toppings)
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza()
# make_pizza(12, 'anchovies')       
# make_pizza(12, 'sausage', 'black olives', 'extra cheese', 'pepperoni')


#3. What type of argument is 12?  Is it required or optional?
#4. What does the # in front of toppings tell Python to expect?



