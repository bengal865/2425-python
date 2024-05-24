#***********************************
# Author: Bruce Provencher
# Project: Restricted Network Access
# Date: 27 NOV 2019
#***********************************

import time

# In this project, we'll use logical operators and
# compound (not single) conditions to grant or deny
# the user access to a restricted network

# Display an initial message to the user when the program loads
print ("\tWelcome to the Area 51 Facility Network.")
print ("\tWARNING: This is a RESTRICTED U.S. Government network.")
print ("\tUnauthorized users will be prosecuted to the fullest extent")
print ("\tof the law.\n\n")

# Set the security level to zero 
# Assign security level to the variable named security

# Set the value of the variable username and the variable password to a null string
# The while loops will loop repeatedly until the user 
# enters a valid username and password

username = ""
password = ""

'''
while not username:
	username = input("Enter your username: ")
	

while not password:
	password = input("Enter your network password: ")
	'''
	
while username == "" and password == "":
	username = input("Enter your username: ")
	time.sleep(1.5)
	print('Verifying username...\nPlease wait...\n')
	time.sleep(1.5)
	password = input("Enter your password: ")
	time.sleep(1.5)
	print('Checking password...\nPlease wait...\n')
	time.sleep(1.5)	
	
	
	# Use a series of if/elif statements to verify the user's username and password

	if username == "ramboj" and password == "afghanistan":
		security = 5
		print ("Welcome,"+ username + "!")
		print ("You have been granted Level ",security,"security clearance")
		print ("for the duration of your stay at Area 51.")

	elif username == "president" and password == "commanderinchief":
		security = 10
		print ("Welcome,",username+ "!")
		print ("You have been granted Level ",security,"security clearance")
		print ("for the duration of your stay at Area 51.")

	elif username == "morrellm" and password == "nokgb":
		security = 8
		print ("Welcome,",username+ "!")
		print ("You have been granted Level ",security,"security clearance")
		print ("for the duration of your stay at Area 51.")
		
	else:
		print ("WARNING: Login failed! Attempted security breach!")
	
input("\n\nPlease press the ENTER key to continue.")


