
# Bruce Provencher
# 24 OCT 2022
# Simple Calculator with Functions

# Define the three functions used in this project
def addition(num1, num2):
    total1 = num1 + num2
    return total1

def subtraction(num1, num2):
    total2 = num1 - num2
    return total2

def multiplication(num1, num2):
    total3 = num1 * num2
    return total3

# Get info from user
name = input(f'Please enter your first name: \n')
num_one = float(input(f'Please enter your first number: \n'))
num_two = float(input(f'Please enter a second number: \n'))

# Define three variables for storing the result of each calculation
addition_total = addition(num_one, num_two)
subtraction_total = subtraction(num_one, num_two)
multiplication_total = multiplication(num_one, num_two)

# Display the results in the terminal 
print(f'Python will now do addition for you, {name.title()}...')
print(f'{num_one:,.2f} + {num_two:,.2f} = {addition_total:,.2f}')
print(f'')
print(f'Python will now do subtraction for you, {name.title()}...')
print(f'{num_one:,.2f} - {num_two:,.2f} = {subtraction_total:,.2f}')
print(f'')
print(f'Python will now do multiplication for you, {name.title()}...')
print(f'{num_one:,.2f} * {num_two:,.2f} = {multiplication_total:,.2f}')
print(f'Thank you for using my simple calculator!')
print(f'Have a good day, {name.title()}!')
input('Press ENTER to quit...')