################################################
# Author: Bruce Provencher
# Project: My Simple Calculator
# Date: 17 JUL 2020
################################################

# Get two numbers from the user (INPUT)
num1 = float(input("Please enter your first number:\n"))
num2 = float(input("Please enter your second number:\n"))

# Processing
# Write the formulas so Python can do the math for us

the_sum = num1 + num2 # Can't name the variable sum because sum is a reserved word in Python
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Display the OUTPUT (results of each calculation)
print(f'{num1} + {num2} = {the_sum}')
print(f'{num1} - {num2} = {difference}')
print(f'{num1} * {num2} = {product}')
print(f'{num1} / {num2} = {quotient}')

# Close the script by pressing the ENTER key
input("Press ENTER to quit...")
