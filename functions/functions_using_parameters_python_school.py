# This program will square a number
# using three functions, all of which are called
# from the main( ) function

# 04 JUN 2018
# Source: Python School
# https://pythonschool.net/basics/functions-with-parameters/

def input_data():
	number = int(input("Please enter a number:\n"))
	return number
	
def process_data(number):
	squared_number = number * number
	return squared_number
	
	
def output_answer(squared_number):
	print("The square of your number is {0}.".format(squared_number))
	
def main():
	# Calling our three functions
	users_number = input_data()
	users_squared_number = process_data(users_number)
	output_answer(users_squared_number)
	
# Call the main function
main()
