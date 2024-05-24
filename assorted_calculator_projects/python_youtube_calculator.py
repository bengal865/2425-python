# Bruce Provencher
# 22 OCT 2022
# Simple Calculator with Menu

import math
# Define the functions for this project

def addition(num1, num2):
    total1 = num1 + num2
    return total1

def subtraction(num1, num2):
    total2 = num1 - num2
    return total2

def multiplication(num1, num2):
    total3 = num1 * num2
    return total3

def division(num1, num2):
    total3 = num1 / num2
    return total3

def calc_square_root(num1):
	answer = math.sqrt(num1)
	return answer

def raise_to_power(num1, num2):
	answer = num1 ** num2
	return answer

while True:

	# User selects a math operation to perform or quits program by entering 'q'
	
	operation = input("Which math operation do you wish to perform? (+ - * / sqrt exp) (q to quit)\n").lower()

	# Quit program if user enters either 'q' or 'Q'
	
	if operation == "q" or operation == "quit":
		
		break

	# What math operation does the user want to perform?
	
	elif operation == "sqrt" :
	
		num1 = float(input("Please enter a number you wish to find the square root of:\n"))
		result = calc_square_root(num1)
		print (f"The square root of {num1:,.2f} is {result:,.2f}.")
		
		
		
	elif operation == "+": 
			
		num1 = float(input("Please enter a number:\n"))

		num2 = float(input("Please enter your second number:\n"))
		
		answer = addition(num1, num2)

		print(f'{num1:,.2f} + {num2:,.2f} = {answer:,.2f}')
		
		
		
	# Subtraction
			
	elif operation == "-":
		num1 = float(input("Please enter a number:\n"))

		num2 = float(input("Please enter a second number:\n"))
		
		answer = subtraction(num1, num2)

		print(f'{num1:,.2f} - {num2:,.2f} = {answer:,.2f}')
		
		
		

	# Multiplication
			
	elif operation == "*":
		num1 = float(input("Please enter a number:\n"))

		num2 = float(input("Please enter a second number:\n"))
		
		answer = multiplication(num1, num2)

		print(f'{num1:,.2f} * {num2:,.2f} = {answer:,.2f}')
		
		


	# Division
			
	elif operation == "/":
			
		num1 = float(input("Please enter your first number:\n"))

		num2 = float(input("Please enter a second number:\n"))
		
		answer = division(num1, num2)

		print(f'{num1:,.2f} / {num2:,.2f} = {answer:,.2f}')
		
		

	# Raise a number to a certain power
			
	elif operation == "exp":
	
		num1 = float(input("Please enter a number:\n"))
		
		num2 = int(input("Please enter an INTEGER for your exponent (Example: 2 for the power of 2):\n"))

		result = raise_to_power(num1, num2)
		
		
		print(f'{num1} raised to the power of {num2} is: {result:,.2f}')
			
	else:
			
		print ("Sorry, invalid menu option!  Please try again!")
	
