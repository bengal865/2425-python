####################################
# Author: Bruce Provencher
# Project: Astronaut Weights
# Date: 24 APR 2018
####################################

# This is a comment!


# This program calculates your weight on the moon and on the sun
# as compared to your weight on Earth


# Ask user to enter his/her weight on Earth
# Convert weight entered (as a string value)
# to an integer by applying the int function

earthWeight = int (input ("Please enter your Earth weight in pounds:\n"))
print ()
print ("Your weight on Earth is:",earthWeight,"pounds")

# Calculate the user's weight on the moon,
# which is only 1/6 of one's weight on Earth

moonWeight = earthWeight / 6
moonWeight = int (moonWeight)

# Print user's weight on the moon
# Ask user if s/he wants to continue

print ("Did you know you'd only weigh",moonWeight, "pounds on the moon?")
input("Press the ENTER key to continue...")

# Calculate the user's weight on the surface of the sun
# Users weigh 27.1 times more on the sun than they do on Earth

sunWeight = earthWeight * 27.1
sunWeight = int (sunWeight)
print ("Better watch those evening snacks, though! On the sun, you'd weigh",sunWeight, "pounds!")
print("Thank you for using my Astronaut Weights script!")

