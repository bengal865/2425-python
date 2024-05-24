# Programmer: Bruce Provencher
# Date: 19 SEP 2016
# Project: Four Function Simple Calculator

# Display a basic welcome message

print ("Hello, welcome to my basic calculator!")
print ("This program will take two numbers from the user")
print ("and then add, subtract, multiply, and divide the numbers")

# Use the input function to get the two numbers from the user

num1 = input ("Please enter your first number: ")
num2 = input ("Please enter your second number: ")

# Convert user input into numbers Python can use to do the math for us
# Tell Python to handle or treat the user input as floating-point numbers
num1 = float(num1)
num2 = float(num2)

# Write some formulas so Python knows how to do the math

# Addition
sum = num1 + num2

# Subtraction 

difference = num1 - num2

# Multiplication

product = num1 * num2

# Division

quotient = num1 / num2

# Show the output to the user

print ("The first number you entered was: " , num1)
print ("The second number you entered was: " , num2)
print ("Sum of the numbers: " , sum)
