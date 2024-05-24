"""
Programmer: Bruce Provencher
Date: 26 JUL 2020
Project: My Simple Calculator

"""

introduction = '''
This script will:

1. prompt the user for his/her first name.
2. welcome the user by his/her first name.
3. prompt the user for two different numbers.

NOTE: The two numbers will be floats/floating-point numbers.

4. Perform three (3) of the four math operations below:

a. addition
b. subtraction
c. multiplication
d. division

5. use concatenation OR f-strings to display the output.

NOTE: Please watch the entire video before you start writing any code.
'''

# Show the introduction
print(introduction + '\n\n')

# Get input from the user
fname = input('Please enter your first name: \n').title()
print(f'Welcome, {fname}!\n')

num1 = float(input(f'Please enter your first number, {fname}: \n'))
num2 = float(input(f'Please enter a second number, {fname}: \n\n'))

# Do the math (processing) and also display the output
print(f'Python will now do subtraction for you, {fname}...')
print(f'{num1} - {num2} = {num1 - num2}')

print(f'Python will now do division for you, {fname}...')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'Python will now do multiplication for you, {fname}...')
print(f'{num1} * {num2} = {num1 * num2}\n\n')
print(f'Thank you for using my simple calculator! Adios, {fname}!')

