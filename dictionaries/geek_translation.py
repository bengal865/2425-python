#****************************************************
# Author: Bruce Provencher
# Project: Geek Translator
# Date: 18 DEC 2012
#****************************************************

# The Geek Translator project makes use of so-called Python dictionaries 

# Step 1: Create a dictionary containing terms and their definitions
# The name of the dictionary in this case will be 'geek'

geek = {"protocol":"An agreed-upon format for transmitting data between two devices. The protocol determines the type of error checking to be used, the data compression method, if any, that will be used, and how the sending device will indicate it has finished sending a message how the receiving device will indicate that it has received a complete, error-free message.", "CSS":"A new feature being added to HTML that gives both Website developers and users more control over how pages are displayed. With CSS, designers and users can create style sheets that define how different elements, such as headers and links, appear. These style sheets can then be applied to any Web page.","web server":"Web servers are computers that deliver (serve up) Web pages.", "graphical user interface":"A program interface that takes advantage of the computer's graphics capabilities to make the program easier to use. Well-designed graphical user interfaces can free the user from learning complex commands needed to install software, run programs, and use the computer's operating system."}

# Code for creating a menu

choice = None
while choice !="0":
	
	
	print (
	"""
	Geek Translator
	
	0 - Quit
	1 - Look Up a Geek Term
	2 - Add a Geek Term
	3 - Redefine a Geek Term
	4 - Delete a Geek Term
	"""
	)
	
	choice = input ("Enter your choice: ")
	print( )
	
# Exit the program if the user selects option zero

	if choice == "0":
		print ("Good-bye!")
		
# Get a definition for the user
	elif choice == "1":
		term = input("Which term do you want me to translate?: ")
		if term in geek:
			definition = geek[term]
			print ("\n", term, "is defined as: ", definition)
		else:
			print ("\nSorry, but I don't know the term", term)
			
# Add a new term to the dictionary using a term-definition pair
	elif choice == "2":
		term = input("Which term do you want me to add to the dictionary?: ")
		if term not in geek:
			definition = input("\nWhat's the definition of the term?: ")
			geek[term] = definition
			print ("\nThank you. The term", term, "has been added to the dictionary.")
		else:
			print ("\nWhoa! That term already exists in the dictionary! Try redefining it!")
# Replace an existing key-value pair if the term already exists in the dictionary
	elif choice == "3":
		term = input("Which term do you want me to redefine?: ")
		if term in geek:
			definition = input("\nWhat's the new definition of the term?: ")
			geek[term] = definition
			print ("\nThank you. The term", term, "has been redefined.")
		else:
			print ("\nWait! That term doesn't exist! Try adding it to the dictionary!")
# Delete a term-definition pair if the user chooses menu option 4 
	elif choice == "4":
		term = input("Which term should I delete?: ")
		if term in geek:
			del geek[term] 
			print ("\nOkay. I just deleted", term, "from the dictionary.")
		else:
			print ("\nStop! I can't do that! That term doesn't exist in the dictionary!")

	else:
		print("Sorry, but", choice, "isn't a valid menu choice!")
		
# Ask the user to continue by having the user press the
# ENTER key

input ("\n\nPlease press the ENTER key to continue...")


