# Programmer: Bruce Provencher
# Date: 20 MAR 2014
# Project: User's Age in Seconds


# 1. asks the user for his/her first name
# 2. asks the user to enter his/her age 
# 3. asks the user to enter the number of days in a year (365)
# 4. asks the user to enter the number of hours in a day 
# 5. asks the user to enter the number of minutes in one hour 
# 6. asks the user to enter the number of seconds in one minute 
# 7. calculates the user's age (expressed in seconds)
# 8. tells the user his/her age (expressed in seconds)
# 9. thanks the user, by first name, for using the program
# 10.  tells the user to 'Press the ENTER key to exit.'

# Ask the user for his/her first name

print ("Greetings!")
firstName = input ("Please enter your FIRST name: \n")

# Prompt user for his/her age in years and convert age to an integer
userAge = int(input ("Please enter your age (in years): \n"))

# Ask user for number of days in a year and convert age to an integer

daysInYear = int(input ("Please enter the number of days in one year: \n"))

# Ask user for number of hours in a day and convert age to an integer
hoursInDay = int(input ("Please enter the number of hours in one day: \n"))

# Ask user for number of minutes in one hour and convert age to an integer

minutesInHour = int(input ("Please enter the number of minutes in one hour: \n"))

# Ask user for number of seconds in one minute and convert age to an integer

secondsInMinute = int(input ("Please enter the number of seconds in one minute: \n"))

# Calculate the user's age (expressed in seconds)

ageInSeconds = userAge * daysInYear * hoursInDay * minutesInHour * secondsInMinute

# Use string function to convert result of calculation into a string, which can be
# concatenated

ageInSeconds = str(ageInSeconds)

# Thank user for using the program
# Display output

print ("Thank you, " + firstName + ", for using the Age in Seconds program.\n")
print ("Expressed in seconds, your age is: " + ageInSeconds)

# Exit program

input ("\n\nPlease press the ENTER key to exit.")
