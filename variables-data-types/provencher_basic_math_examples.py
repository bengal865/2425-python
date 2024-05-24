# Programmer: Bruce Provencher
# Date: 10 SEP 2014
# Project: Basic Math & Input ( ) Function Demo

# Declare (create) our variables for this program





# Get the input from our user

num1 = input ("Please enter your first number: ")
num2 = input ("Please enter your second number: ")
num3 = input ("Please enter your third number: ")
num4 = input ("Please enter your fourth number: ")

# Take the user's input and convert it from text into actual numbers

num1 = int (num1)
num2 = int (num2)
num3 = int (num3)
num4 = int (num4)



# Write an equation to tell Python how to add up
# the four numbers

sumOfNumbers = num1 + num2 + num3 + num4

# Now get Python to show the answer

sumOfNumbers = str(sumOfNumbers)

print ("Your answer is: " + sumOfNumbers)


