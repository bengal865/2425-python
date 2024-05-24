
# Create a Python list containing 6 elements
# Here, each element represents the distance between two
# cities in miles
destinations = ['Traverse City', 'Houghton Lake', 'Suttons Bay', 'Elk Rapids', 'Acme', 'Mancelona']
driving_distances = [50, 35, 75, 62, 41, 44]


# Set up your FOR loop so you can tell Python to move through
# the list, one element at a time (sequentially)

#print ("The distances contained in your list are:\n")
print ("The distance you are pointing to is:\n")
#print (driving_distances[5], "miles")

# 'miles' points to the index number for each element

for x in range(len(driving_distances)):
	print (f'{destinations[x]}: driving_distances[x])

