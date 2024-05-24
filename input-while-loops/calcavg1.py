#################################
# Author: Bruce Provencher
# Project: Practicing with User-Defined Functions
# Date: 09 FEB 2013
#################################

# This project uses a user-defined function
# along with an if-statement


print ("Welcome to my program!\n")

# Define the function

def calcavg(count):
    """This function calculates the average of two numbers and displays the result."""
    sum = num1 + num2
    numavg = sum / count
    print ("Your average is: ", numavg)




# Ask the user if s/he would like to continue


count = 1
response = "y"



while response == "y":

    input ("This program will average two numbers for you.  Input your two numbers below. [Press ENTER to continue ...] ")



# Get user input

    num1 = float(input("Please enter a positive number greater than zero: "))


    if num1 <= 0:
        count = count - 1
        print ("Stop! Please enter a POSITIVE number greater than zero!")
        num1 = float(input ("Your first positive number greater than zero is: "))
    else:
        num1 = float(num1)

    num2 = float(input("Please enter another positive number greater than zero: "))


    if num2 <= 0:
        count = count - 1
        print ("Stop! Please enter another POSITIVE number greater than zero!")
        num2 = float(input("Your second positive number greater than zero is: "))

    else:
        num2 = float(num2)
    count = count + 1
    calcavg(count)

    response = input("Do you wish to average another pair of numbers? ['y' to continue, 'n' to quit]: ")




