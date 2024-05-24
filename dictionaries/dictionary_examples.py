#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################
# Author: Bruce Provencher
# Project: Working with Dictionaries (Various Examples)
# Date: 17 FEB 2013
###############################

# Note the use of curly braces { }
# when creating your dictionary
# Below we have an empty dictionary named
# my_dictionary

my_dictionary = {}


# Create a new dictionary containing a single item
# Must add a key:value pair when you want to add items
# to a Python dictionary

# You can mix and match key data types in the same dictionary
# Below we have a string as our key ('Jan')

days_in_month = {'Jan':31}

# To print out the number of days in the month of January, provide
# Python with the key to get access to its value (key:value pair)
print ("The number of days in the month of January is:\n")
print (days_in_month['Jan'])

# To add more than one key:value pair to a dictionary, separate each
# key:value pair with a comma

days_in_month = {'Jan':31, 'Feb':28, 'Mar':31}

# Can also write the same three key:value pairs on separate lines

days_in_month = {'Jan':31,'Feb':28,'Mar':31}

# You can print a single item from a dictionary or the entire
# dictionary

# To print the entire dictionary, write this code:
print ("The dictionary currently contains the following information:\n")
print (days_in_month)

# You can also use several different methods with dictionaries
# Tell Python to print all the keys in your dictionary using the keys () method
# NOTE: This method returns a list structure
# Could store the list in a variable for future use

print ("The dictionary currently contains the following information:\n")
print (days_in_month)
print ("Now print only the keys found in the dictionary:")
print (days_in_month.keys())


# You can also print just the values in the dictionary using the values ( ) method
# NOTE: This method also returns a list structure
# Could store the list in a variable for future use
print ("The dictionary currently contains the following information:\n")
print (days_in_month)
print ("Now print ONLY THE VALUES found in the dictionary:")
print (days_in_month.values())

print("Use the items ( ) method to return a list of key:value tuples")
print ("NOTE: Tuples are immutable and are displayed inside parentheses")

print (days_in_month.items())
print ()
print ()
print ("How to add items to a dictionary")
print ()
print ("Add the month of April and the number of days in April to our existing dictionary")
print ("Type the key inside square brackets")
print ("Assign the value you want associated with the key with an equal sign followed by the value")
days_in_month ['Apr']=30
print (days_in_month)
print ()
print ("You can also combine multiple dictionaries using the update () method")
# Print the original dictionary
print ("The original dictionary contains these key:value pairs:\n")
print (days_in_month)
# Create a second dictionary, which will be combined with the original dictionary
days_in_month2 = {'May':31, 'Jun':30, 'Jul':31}
# Now combine the two dictionaries
days_in_month.update(days_in_month2)
# Print the combined dictionary
print (days_in_month.keys())
print ("Print the keys for the days_in_month2 dictionary")
print (days_in_month2.keys())


# Use the DEL keyword to remove an item from a dictionary
# To remove the key:value pair of Apr:30:

del days_in_month['Apr']

# If the key isn't in the dictionary, you'll get a KeyError message
# Should first check to see if the key is present by using the keyword 'in'

# May want to remove all items in the dictionary at some point
# Use the clear () method to do this
# Remember: The keyword DEL only deletes a single item, not all the items in
# the dictionary

breakfast = {'eggs':'bacon', 'butter':'toast', 'coffee':'sugar'}
dinner = {'steak':'fries', 'salad':'dressing', 'apple pie':'ice cream'}

print (breakfast)
# print ()
# print (dinner)
# print ()
# To remove all items in the breakfast dictionary, use the clear () method
# breakfast.clear()
# Now print the breakfast dictionary to check that it's empty
# print (breakfast)
# print ()
# del dinner
# Print the dinner dictionary
# print ("Now print the dinner dictionary")
# print (dinner)

# To avoid KeyError messages when you try to access a key that doesn't exist in
# a dictionary, use the get () method and provide a default value to be returned if in fact
# the key doesn't exist

# print (breakfast)
# 'None' will be returned since the key 'cereal' doesn't exist in the dictionary
print (breakfast.get('cereal'))
print ()
print ("Provide a default value that will be displayed instead of 'None' if the key")
print ("isn't in the dictionary\n")
print (breakfast.get("cereal", "The key 'cereal' is not present in the breakfast dictionary"))

# Create a new dictionary named 'words'
words = {}
value = input("Please enter a word (or -999 to quit the program):")
while (value !='-999'):
    if value in words:
        words [value] = words[value] + 1
    else:
        words[value] = 1
    value = input("Please enter a word (or -999 to quit the program):")

# for current_key in words.keys():
#   print (current_key, "\t", words[current_key])

# The Python function list as used below will take the list of keys returned
# to us by the keys method and allow us to store them as an actual Python list (minus the dict_keys output)
# We can then sort the keys using the sort () method
my_keys = list(words.keys())
my_keys.sort()

for current_key in my_keys:
    print (current_key, "\t", words[current_key])
