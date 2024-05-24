# Programmer: Bruce Provencher
# Date: 15 NOV 2018
# Project: Passing Values Into/Out of Functions

def input_data():
	number = int(input("Please enter a number:\n"))
	return number
	
def process_data(number):
	# Tell Python to square the original number
	squared_number = number ** 2
	return squared_number
	
def output_the_answer(number, squared_number):
	print(f"Your original number: {number}")
	print(f"Your number squared is: {squared_number}")
	
def main():
	users_number = input_data()
	users_squared_number = process_data(users_number)
	output_the_answer(users_number, users_squared_number)
	
# Call the function named 'main'
main()







