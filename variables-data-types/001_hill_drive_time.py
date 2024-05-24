# Programmer: Nick H.
# Date: 19.09.2018
# Project: Drive

# Prompts user for distance and speed, and converts the input into integers
distance = int(input("How many miles are you driving? "))
mph = int(input("How fast are you travelling? (in MPH) "))

# Calculates travel time
travelTime = round(distance / mph, 1)

# Displays distance, mph, and travel time
print()
print(f"Distance: {distance} miles")
print(f"Miles per Hour: {mph} mph")
print()
print(f"Travel time: {travelTime} hours") 
