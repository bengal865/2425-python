# Programmer: Bruce Provencher
# Date: 15 MAR 2014
# Project: Get the User's Age 

# Use Python's input function to ask Ask user for his/her age

userAge = input ("Please enter your age: ")

# Convert text input to an integer so Python can take the user's age and
# add ten years to it

# Reminder: An integer is a number that doesn't have a decimal point

userAge = int(userAge)

# Add 10 years to the user's age, then have Python display the new age

newAge = userAge + 10

# Display the message to the user first, followed by the user's new age
# Use the COMMA to separate the string from the numeric value (the user's age
# plus ten years)

# On the line of code below, then, we are telling Python to display a string followed by a numeric
# value (a number) -- so we are not converting the number into a string in this instance

print ("Your age plus ten years is:",  newAge)

# Use another built-in Python function -- the string function -- to
# convert a number back into a string

# Then join the first string to the second string to create
# a longer string (the final output for this project)

#print ("Your age plus ten years is:" + str(newAge))



