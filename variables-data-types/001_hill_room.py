# Programmer: Nick H.
# Date: 19.09.2018
# Project: Room

# Stores base and height lengths
base = 12.5
height = 16.7

# Calculates area and perimter, rounding the area
area = round(base * height, 1)
perimeter = ( base * 2 ) + ( height * 2 )

# Displays sentences describing the area and perimeter
print(f"The area of your room is {area} sq. meters.")
print(f"The perimeter of your room is {perimeter} meters.")
