#########################
# Name: Bruce Provencher
# Project: List Append Method
# Date: 15 FEB 2013
#########################

# This project demonstrates how to use the append
# method to add items to a Python list

# Create an empty list named movies

movies = []

# Use the append method to add an element to your movies list
# You can only append one item at a time to a list!
# Trying to append more than 1 item at a time to your list will generate an error!


# Display your updated list of movies below this line



# It's also possible to CONCATENATE lists in Python, just like you can concatenate strings
# Use the + concatenation operator to join multiple lists
us_states = ['Missouri', 'California', 'Arizona', 'Texas']
us_states = us_states + ["Iowa", "Kentucky", "Idaho"]
# Use the concatenation operator to concatenate a list of TWO of your favorite movies to your existing list of movies

# Now display your updated list of movies below this line


# You can also insert an element into your list by referencing
# a specific index number 

# Example: Adding the element 'New Mexico' to my list of U.S. states at index number 2...
print ("My original list of states was: ")
print (us_states)
us_states.insert(2, "New Mexico")
print ()

# Use the insert ( ) method to add a Disney movie at a specific index number to your movies list 


# You can use the REMOVE method to remove elements from a list
# Here I'm removing the element 'Iowa' from my list of U.S. states...
us_states.remove("Iowa")
print (us_states)
print ()
print ()

# The REVERSE method allows you to display your list items in reverse order
print ("Currently, my us_states list is arranged like this:")
print (us_states)
print()
print ("After applying the REVERSE method to our list, my us_states list is now arranged like this: ")
us_states.reverse()
print (us_states)
print()
print()
# The SORT method allows you to sort your list items in increasing order
weekdays = ["Tuesday", "Monday", "Friday", "Wednesday", "Thursday", "Sunday", "Saturday"]
print (weekdays)
print()
print ("The weekdays looks like this after we apply the sort ( ) method to it:")
weekdays.sort()
print (weekdays)


