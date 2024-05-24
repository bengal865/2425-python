########################################
# Programmer: Bruce Provencher	
# Date: 00 NOV 2018										
# Project: WHILE Loop / Manipulating A Python List																					
#######################################
import time
# Create my Python list of crusader gear

gear = ["banner", "sword", "magic potion"]

# Text menu in Python
      
def print_menu():       
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Show the list")
    print ("2. Add an item to list")
    print ("3. Delete an item from list")
    print ("4. Insert an item into the list")
    print ("5. Count/display the number of items in the list")
    print ("6. Clear the entire list")
    print ("7. Exit")
    print (67 * "-")
  
  
def show_list():
	print("Here is your current list:")
	print(gear)
	

	
def append_list_item(list_item):
	"""Function for appending an item to the list"""
	print("Appending your item to the list of supplies...")
	# In this example, 'gear' is the name of my list
	gear.append(list_item)


def remove_list_item (index):
	"""Remove an item from the list"""
	if index >= 0 and index < len(gear):
		print("Removing the item from your list of supplies...")
		gear.pop(index)
	else: 
		print("Sorry, that index number is out of range.")
		print(f"Your index number must be a number from 0 to {len(gear) - 1}.")
		print("Please try again.")
		print_menu()

def insert_list_item (index_num, list_item):
	"""Insert an item into the list at specified index number"""
	gear.insert(index_num, list_item)
	
def empty_entire_list():
	"""Clear the entire list"""
	print("Clearing your entire list...")
	time.sleep(2)
	print("Please wait...")
	gear.clear()
	time.sleep(1)
	print("You now have an empty list.")
	show_list()
	
def display_length_of_list():
	print(f"You are currently carrying {len(gear)} item(s) with you on your crusdade.")
	show_list()

keep_looping = True      
# While loop keeps looping until variable 'keep_looping' is set to False 
while keep_looping:
	  
	print_menu() 
	
	menu_choice = int(input("Please choose an option (1 - 7):\n"))
	
	if menu_choice == 1:
		show_list()
		
	elif menu_choice == 2:
		list_item = input("Enter an item to add to your list: (Example: lance)\n")
		append_list_item(list_item)
		show_list()

		
	elif menu_choice == 3:
		at_index = int(input("Enter index number for the item to delete from your list: (Example: 3)\n"))
		if at_index >= 0 and at_index < len(gear):
			remove_list_item(at_index)
			print("And here is your updated list of supplies:")
			show_list()
			print()
			print()
		else:
			print("Sorry, that index number is out of range.")
			print(f"Your index number must be a number from 0 to {len(gear) - 1}.")
			print("Please try again.")
			print_menu()
			
	elif menu_choice == 4:
		print("Preparing to insert an item into your list of supplies.")
		time.sleep(2)
		print("Please wait...")
		time.sleep(2)
		at_index = int(input("At which index number should I insert your list item? (Example: 2)\n"))
		time.sleep(2)
		list_item = input("Enter an item to insert into your list of supplies: (Example: mace)\n")
		
		insert_list_item(at_index,list_item)
		show_list()
		print()
		print()
	
	elif menu_choice == 5:
		display_length_of_list()
	
	elif menu_choice == 6:
		empty_entire_list()	
		
	elif menu_choice == 7:
		keep_looping = False
		break
	else:
		print("Invalid selection! Please choose another menu option!")
		
print("Thank you for keeping your crusader's list of gear up to date.")
print("May you be victorious on your crusade, oh brave one!")
time.sleep(1)
print("Farewell!")

	
	
