
# Programmer: 
# Project: Network Password Check
# Date: 

import time
import sys

def show_area51_message():
	# Display an initial message to the user when the program loads
	print ("\tWelcome to the Area 51 Facility Network.")
	print ("\tWARNING: This is a RESTRICTED U.S. Government network.")
	print ("\tUnauthorized users will be prosecuted to the fullest extent")
	print ("\tof the law.\n\n")
	
def get_username():
	username = input("Enter your username ('q' to quit):\n")
	time.sleep(1.5)
	if username == "q" or username == 'quit':
		keep_looping = False
		print('Exiting system...\nPlease wait...\n')
		time.sleep(1.5)
		print('Goodbye!')
		time.sleep(1)
		sys.exit()
	else:
		print('Verifying username...\nPlease wait...\n')
	time.sleep(1.5)
	return username

def get_password():
	password = input("Enter your password:\n")
	time.sleep(1.5)
	print('Checking password...\nPlease wait...\n')
	time.sleep(1.5)	
	return password
	
def display_clearance(username, clearance):
	print (f"Welcome, {username}!")
	print (f"You have been granted Level {clearance} security clearance")
	print ("for the duration of your stay at Area 51.")
	
username = ""
password = ""


show_area51_message()


keep_looping = True
while keep_looping:
	
	user = get_username()
	pwd = get_password()
	
	if user == "ramboj" and pwd == "afghanistan":
		level = 5
		display_clearance(user, level)

	elif user == "president" and pwd == "commanderinchief":
		level = 10
		display_clearance(user, level)

	elif user == "morrellm" and pwd == "nokgb":
		level = 8
		display_clearance(user, level)
		
	else:
		print ("WARNING: Login failed! Attempted security breach!")
	
input("\n\nPlease press the ENTER key to continue.")


