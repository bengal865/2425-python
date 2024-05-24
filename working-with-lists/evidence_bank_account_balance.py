
# Bruce Provencher
# 14 OCT 2022
# Evidence: Bank Account Balance

# Import my modules
import random
import time

# Declare and initialize variables

# Use randint ( ) method to generate account balance 
# between -10 and 50 dollars (could include -10 or 50)
balance = random.randint(-10, 50)
first_name = ''
penalty = 25.00 # Set penalty fee of $25.00

introduction = 'This script will check the user\'s account balance and display a message'
introduction += ' about his/her current account balance.'

time.sleep(2)

# Display introduction
print()
print(introduction)
time.sleep(2)


# Get first name from user
first_name = input('Please enter your first name:\n')
time.sleep(2)

# Check account balance and display message about user's bank account balance
if balance < 0:
    print(f"Your balance, {first_name.title()}, is below 0, so add funds now or you will be charged a penalty of ${penalty:,.2f}.")
 
elif balance == 0:
    print(f"Your account balance, {first_name.title()}, is at zero! Please add funds to your account soon!")
 
else:
    print(f"Your account balance, {first_name.title()}, is currently ${balance:,.2f}.  No action necessary at this time.")



time.sleep(2)
print(f'Thank you for using the Bank Account Balance Checker, {first_name.title()}!')
time.sleep(2)

input('Press ENTER to continue...')