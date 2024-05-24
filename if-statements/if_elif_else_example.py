# Bruce Provencher
# If/Elif/Else Example
# 23 SEP 2022

# One outcome

temperature = 20

if temperature < 32:
	print('It\'s cold outside!')


# # Two possible outcomes
# choice = 0
# print('What is your citizenship?')
# print('1. French')
# print('2. German')
# choice = int(input('Enter 1 or 2:\n'))

# if choice == 1:
# 	print(f'You have French citizenship.')
# else:
# 	print(f'You have German citizenship.')


# Multiple outcomes (more than two)
year = input("Enter your year in college (1 - 4):")

if year == "1":
	print ("You are a freshman in college!")
	print()
elif year == "2":
	print ("You are a sophomore in college!")
	print()
elif year == "3":
	print ("You are a junior in college!")
	print()
elif year == "4":
	print ("You are a senior in college!")
	print()

# The else statement is used to 
# handle invalid user input

else:
	print ("Invalid entry! Please enter a number between 1 and 4 only!")
	print()

					
					
