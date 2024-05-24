# Programmer: Bruce Provencher
# Date: 19 SEP 2014
# Project: Crusader Equipment List

# Can only assign a single value to a variable, but
# you can assign multiple values to a list

# Creating a list to hold the crusader's gear

gear = ["banner","sword","map"]

print("""
# Programmer: Bruce Provencher
# Date: 19 SEP 2016
# Project: Crusader Equipment List
""")

# Print the entire list
print (gear)

# Slicing the list
print ("The crusader took his", gear[1], "and his", gear [0], "into battle.")
print ("May he be victorious!")

# Changing a list element
print ("Changing the third element in the list...\n")
print (gear)
gear [2] = "mace"
print ("Third list element is now: ", gear[2])
print (gear)


# Can use the .append ( ) method to add items to the list
# after you've created the list

print ("Adding a leather satchel to the revised list...")
gear.append("leather satchel")
print (gear)

