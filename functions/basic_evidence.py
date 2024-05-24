'''
Programmer: Garrett Sedwick
Date: 09 30 2020
Project: Basic Evidence
'''
import time

# I decided to use functions because they make the script look cleaner
# than doing the math in the output.
def addition(number1, number2):
	result = number1 + number2
	return result 
def subtraction(number1, number2):
	difference = number1 - number2
	return difference
def multiplication(number1, number2):
	product = num1 * num2
	return product

# I Add an extra line to my input because I think it looks better when
# the user responds on the line below the question.
fname = input('''Please enter your first name: 
''')
print(f'''Welcome, {fname}!
''')
num1 = float(input(f'''Please enter your first number, {fname}: 
'''))
num2 = float(input(f'''Please enter your second number, {fname}:
'''))

# I made one output for all math equations using a comment block, this
#  makes the code look cleaner in my opinion
print(f''' 
Python will now find the sum for you, {fname}...
{num1} + {num2} = {addition(num1, num2)}
Python will now find the difference for you, {fname}...
{num1} - {num2} = {subtraction(num1, num2)}
Python will now find the product for you, {fname}...
{num1} * {num2} = {multiplication(num1, num2)}
''')

print(f'''Thank you for using my simple calculator! Adios {fname}!
''')

# I added a time.sleep so the script could wait a second before
# prompting the user to exit the program.
time.sleep(1)
input('Please Press ENTER to exit.')
