
####################################
# Author: Bruce Provencher              
# Barebones Calculator 
# Date: May 10, 2014                
####################################


# Intro Function
def intro():
	print("Welcome to the Barebones Calculator!")
	print("This calculator can perform addition, subtraction, multiplication, and division.")

	input("Press ENTER TO CONTINUE...\n")

# Menu Function
def menu():
	
	print("Menu Options:")
	print("1: Add")
	print("2: Subtract")
	print("3: Multiply")
	print("4: Divide")
	print("5: Quit")

# Restart Function
def restart():
	repeat = input("Would you like to perform another calculation? (y/n) ")
	repeat = repeat.lower()
	return repeat

# Addition Function
def addition(num1,num2):
	total = num1 + num2
	return total

# Subtraction Function
def subtraction(num1,num2):
	total = num1 - num2
	return total

# Multiplication Function
def multiplication(num1,num2):
	total = num1 * num2
	return total

# Division Function
def division(num1,num2):
	total = num1 / num2
	return total



# Begin program:

repeat = "y" # Sets repeat to 'y' for initial round

option = None

intro()

menu()


while repeat == "y": # Keeps looping until the user quits the program
	

	# Display menu options, then get the user's choice

	option = int(input("Please select a menu option! (1 - 5) "))
	

	if option == 1:
		num1 = float(input("Enter the number you're starting with: "))
		num2 = float(input("Enter the number you're going to add to the first one: "))
		print(num1, "plus", num2, "equals", addition(num1,num2))
		repeat = restart()
	elif option == 2:
		num1 = float(input("Enter the number you're starting with: "))
		num2 = float(input("Enter the number you're going to subtract from the first one: "))
		print(num1, "minus", num2, "equals", subtraction(num1,num2))
		repeat = restart()
	elif option == 3:
		num1 = float(input("Enter the number you're starting with: "))
		num2 = float(input("Enter the number you're going to multiply the first one by: "))
		print(num1, "times", num2, "equals", multiplication(num1,num2))
		repeat = restart()
	elif option == 4:
		num1 = float(input("Enter the number you're starting with: "))
		num2 = float(input("Enter the number you're going to divide the first one by: "))
		print(num1, "divided by", num2, "equals", division(num1,num2))
		repeat = restart()
	elif option == 5:
		print("Thank you for using the Barebones Calculator!")
		repeat = "n"
	else:
		print("ERROR: Invalid Menu Option.")
		menu()
	



