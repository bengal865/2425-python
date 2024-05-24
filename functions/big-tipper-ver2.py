# SOLUTION: Big Tipper 2.0
# 15 MAR 2021

import time


def welcome_user():
    '''Function that welcomes user to the restaurant by first name.'''
    fname = input('Please enter your first name:\n')
    time.sleep(1)
    print(f'Welcome to Denny\'s, {fname}!')


def calc_subtotal():
    '''Function that calculates the user's subtotal.'''
    prices = []
    num_items = int(
        input('Enter the number of menu items you wish to order today: (Example: 4)\n'))
    # User enters the price of each item ordered from the menu
    for x in range(num_items):
        price = float(
            input(f'Enter the price of menu item #{x + 1}: (Example: 6.99)\n'))
        prices.append(price)

    # Use sum () function to calculate the subtotal
    customer_subtotal = sum(prices)
    return customer_subtotal


def calc_sales_tax(my_subtotal, mi_rate=0.06):
    mi_sales_tax = mi_rate * my_subtotal
    return mi_sales_tax


def calc_tip(my_subtotal, mich_tax):
    TIP_PERCENTAGE = 0.15
    tip = TIP_PERCENTAGE * (my_subtotal + mich_tax)
    return tip


def calc_grand_total(my_subtotal, mich_tax, tip):
    grand_total = my_subtotal + mich_tax + tip
    return grand_total


# Function calls
subtotal = calc_subtotal()
state_tax = calc_sales_tax(subtotal)
the_tip = calc_tip(subtotal, state_tax)
total_bill = calc_grand_total(subtotal, state_tax, the_tip)

# Generate the output
time.sleep(1.5)
print('Receipt for today:\n')
time.sleep(1)
print(f'Subtotal: ${subtotal:,.2f}')
time.sleep(1)
print(f'MI Sales Tax: ${state_tax:,.2f}')
time.sleep(1)
print(f'Tip (@ 15%): ${the_tip:,.2f}\n')
time.sleep(1)
print(f'Grand Total: ${total_bill:,.2f}')
time.sleep(1)
print('Thank you for dining with us today at Denny\'s!')
time.sleep(1)
print('Goodbye!\n')
