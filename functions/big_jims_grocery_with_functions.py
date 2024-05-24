import time


def show_welcome_msg():
  time.sleep(2)
  '''Function that displays a welcome message to the user.'''
  print('Hello, and welcome to Big Jim\'s Country Store!')
  time.sleep(2)
  print('We hope you enjoy shopping at our store today!\n')


def show_introduction():
  '''Function that explains to the user what the script will do.'''

  print('This script will prompt you for the prices of')
  print('five items you purchased today at Big Jim\'s Country Store.\n')
  time.sleep(2)
  print('It will then calculate and display the subtotal, state sales tax,')
  print('and grand total for your purchase.')
  print()
  input('Press any key to continue...')


def get_prices():
  '''Function that will prompt user to enter the prices of five store items.'''
  x = 0
  prices = []
  ordinals = ['first', 'second', 'third', 'fourth', 'fifth']
  while x < len(ordinals):
    price = float(
      input(f'Enter the price of the {ordinals[x]} item: (Example: 4.99)\n'))
    prices.append(price)
    x += 1
  return sum(prices)


def calc_sales_tax(order_subtotal):
  '''Function that calculates the subtotal for the grocery order.'''
  sales_tax_rate = 0.06
  return order_subtotal * sales_tax_rate


def calc_grand_total(order_subtotal, michigan_sales_tax):
  '''Function that calculates the grand total for the grocery order.'''
  return order_subtotal + michigan_sales_tax


def display_output():
  subtotal = get_prices()
  state_tax = calc_sales_tax(subtotal)
  final_total = calc_grand_total(subtotal, state_tax)
  print('Calculating...Please wait...')
  time.sleep(3)
  print(f'Order Subtotal: ${subtotal:,.2f}')
  time.sleep(2)
  print(f'State Sales Tax: ${state_tax:,.2f}')
  time.sleep(2)
  print(f'Grand Total: ${final_total:,.2f}')
  time.sleep(2)
  print('Thank you for shopping at Big Jim\'s Country Store!')
  time.sleep(2)
  input('Press ENTER to continue...')


def main():
  show_welcome_msg()
  show_introduction()
  display_output()


main()