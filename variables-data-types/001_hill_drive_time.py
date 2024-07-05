# Student name
# Current date
# Calculating Travel Time

# Prompts user for distance and speed, and converts the input into integers
distance = int(input("How many miles are you driving? "))
mph = int(input("How fast are you travelling? (in MPH) "))

# Calculates travel time
travel_time = round(distance / mph, 1)

# Displays distance, mph, and travel time
print()
print(f"Distance: {distance} (miles)")
print(f"Miles per hour: {mph} mph")
print()
print(f"Travel time: {travel_time} (hours)") 
