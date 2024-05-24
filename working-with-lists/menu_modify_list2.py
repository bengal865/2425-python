# Programmer: Bruce Provencher	
# Date: 11 NOV 2020									
# Project: WHILE Loop / Manipulating A Python List																					

import time

      
def print_menu():       
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Show the list")
    print ("2. Add an item to list")
    print ("3. Delete an item from list")
    print ("4. Quit")
    print (67 * "-")
    print('\n')
  
  
def show_list(my_list):
	print("Here is your current list:")
	print(my_list)
	print('\n')
	

	
def append_list_item(my_list, list_item):
	"""Function for appending an item to the list"""
	print("Appending your item to the list of supplies...")
	my_list.append(list_item)


def remove_list_item (my_list, index):
	"""Remove an item from the list"""
	if index >= 0 and index < len(my_list):
		print("Removing the item from your gear list...")
		my_list.pop(index)
	else: 
		print("Sorry, that index number is out of range.")
		print(f"Your index number must be a number from 0 to {len(my_list) - 1}.")
		print("Please try again.")
		print_menu()

def insert_list_item (my_list, index_num, list_item):
	"""Insert an item into the list at specified index number"""
	my_list.insert(index_num, list_item)
	
def empty_entire_list(my_list):
	"""Clear the entire list"""
	print("Clearing your entire list...")
	time.sleep(2)
	print("Please wait...")
	my_list.clear()
	time.sleep(1)
	print("You now have an empty list.")
	show_list()
	
def display_length_of_list(my_list):
	print(f"You are currently carrying {len(my_list)} item(s) with you on your crusade.")
	show_list()
	
gear = ["banner", "sword", "magic potion"]

keep_looping = True      
# While loop keeps looping until variable 'keep_looping' is set to False 
print_menu()

while keep_looping:
	  
	print_menu() 
	
	menu_choice = int(input("Please choose a menu option (1 - 4):\n"))
	
	if menu_choice == 1:
		show_list(gear)
		
		
	elif menu_choice <= 0 or menu_choice > 4:
		print("Invalid selection! Please choose another menu option!")
		print_menu()
		
	elif menu_choice == 2:
		list_item = input("Enter an item to add to your list: (Example: lance)\n")
		append_list_item(gear, list_item)
		show_list(gear)

		
	elif menu_choice == 3:
		at_index = int(input("Enter index number of the item to delete from your list: (Example: 3)\n"))
		if at_index >= 0 and at_index < len(gear):
			remove_list_item(gear, at_index)
			show_list(gear)
			print()
			print()
		else:
			print("Sorry, that index number is out of range.")
			print(f"Your index number must be a number from 0 to {len(gear) - 1}.")
			print("Please try again.")
			print_menu()
			

		
	elif menu_choice == 4:
		keep_looping = False
		break

		
print("\nThank you for keeping your crusader's gear list updated.\n")
print("May you be victorious on your crusade, oh brave warrior!")
time.sleep(1)
print("Farewell!")

	
	
