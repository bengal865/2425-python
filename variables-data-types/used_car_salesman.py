#****************************************************
# Author: Bruce Provencher
# Project: Used Car Salesman Project
# Date: 19 NOV 2012
#****************************************************

# This program asks the user to enter the base price of the car s/he wants to purchase
# The program then adds several extra fees to the base price of the car
# The extra fees will be sales tax, licensing, a dealer prep fee, and
# a destination (shipping) charge
# Make the sales tax and licensing fee a percentage of the car's base price
# The remaining fees should be assigned as values to variables
# Display the final price of the car once all the extra fees have been applied

import time

# Welcome the user to the program
welcome = "Welcome to Fast Joey's Used Car Lot!"
print (welcome)
print ("You won't believe the deal we're going to cut you today!")
input ("\n\nPlease press the ENTER key to continue...")

# Next, set the initial values used in the program
basePrice = input ("Before we can start wheeling and dealing, please enter the BASE PRICE of the car you're interested in buying from us today: ")

basePrice = int (basePrice)

#input("\n\nPlease press the ENTER key to continue...")

time.sleep(3)

print ("Guess what?")
print ("There are a couple extra charges we forgot to tell you about...")
print ("So maybe we should tack them onto the base price, so you can see")
print ("how much your car REALLY costs!")
print ()
print ()
time.sleep (2)
input("\nPlease press the ENTER key to continue...")

# Create additional variables and assign values to the variables
# we'll be using in this project

salesTaxRate = 0.06 # Set at 6 percent of the car's base price
salesTax = 0.00
licensingPercentage = 0.02 # Set at 2 percent of the car's base price
licensingFee = 0.00 # Initialize the variable licensingFee to zero before doing the calculations for this project

dealerPrepFee = 125.00
destinationCharge = 250.00
finalCarCost = 0.00

# Calculate the sales tax the purchaser will have to pay on the car

salesTax = basePrice * salesTaxRate

# Calculate the licensing fee the buyer will have to pay on the car

licensingFee = basePrice * licensingPercentage

# Now calculate the final cost of the car 
finalCarCost = basePrice + salesTax + licensingFee + dealerPrepFee + destinationCharge

print ()
print ()

print ("Well, it looks like today is your lucky day at Fast Joey's Used Car Lot!")
print ("The base price of your car was: ${:,.2f}".format(basePrice)+".")
print ("You're going to pay ${:,.2f}".format(salesTax), "in sales tax for your car.")
print ("The licensing fee comes to: ${:,.2f}".format(licensingFee)+".")
print ("Oh, yes, and don't forget to add the dealer prep fee, which comes to ${:,.2f}".format(dealerPrepFee)+".")
print ("And one more thing.  We forgot to add the destination charge for the vehicle, which comes to ${:,.2f}".format(destinationCharge)+".")
print ("So, you got a SUPER deal today at Fast Joey's!")
print ("The final cost for your vehicle today is ${:,.2f}".format(finalCarCost)+".")
print ("Thanks for doing business at Fast Joey's, where hidden fees and fast")
print ("talking are the name of the game, 24/7/365!")

