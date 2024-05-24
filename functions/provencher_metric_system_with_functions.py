# *********************************
# Author: Bruce Provencher
# Project: Metric System
# Date: 10 NOV 2020
# *********************************

def intro():
	print("This program will convert the number of miles the user enters")
	print("into kilometers.\n")
	

def miles_to_km(num_miles):

	conversionFactor = 1.60934
	km = num_miles * conversionFactor
	print(f'Miles: {num_miles:,.2f}')
	print(f'Miles to kilometers (km): {km:,.2f}')

# Call each function
intro()

# Get number of miles from the user
miles = float(input("Enter the number of miles (Example: 20.0) \n"))

miles_to_km(miles)


