# Bruce Provencher
# Basic Calculator 1.0

import sys

def calculate():
  operation = input('''
  Please select the math operation you'd like to run:

  + for addition
  - for subtraction
  * for multiplication
  / for division

  ''')

  num1 = float(input('Enter your first number:\n'))
  num2 = float(input('Enter your second number:\n'))

  if operation == '+':
    # Addition
    print('{0} + {1} = '.format(num1, num2))
    print(num1 + num2)

  elif operation == '-':
    # Subtraction
    print('{0} - {1} = '.format(num1, num2))
    print(num1 - num2)

  elif operation == '*':
    # Multiplication
    print('{0} * {1} = '.format(num1, num2))
    print(num1 * num2)

  elif operation == '/':
    # Division
    print('{0} / {1} = '.format(num1, num2))
    print(num1 / num2)

  else:
    print('Invalid selection! You entered an invalid operator.  Please run the script again.')

  # Call the again ( ) function
  again()

def again():
  go_again = input('''
  Do you want to run the calculator script again? 
  (y/n)''')

  # Convert user input to LOWERCASE by applying the lower() method 
  if go_again.lower() == 'y':
    calculate()

  elif go_again.lower() == 'n':
    print('Thank you for using my calculator script.  Goodbye!')
    sys.exit()
  else:
    again()

def main():
  calculate()

main()