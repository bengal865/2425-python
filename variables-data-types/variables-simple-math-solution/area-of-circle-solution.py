# Calculate area of a circle using a CONSTANT

# Define the constant PI
PI = 3.14159

# Get input
radius_length = float(input('Enter radius length in feet (Example: 12. 5)\n'))

# Process
area_of_circle = PI * ( radius_length ** 2 )

# Output
print(f'Radius of circle (in ft.): {radius_length}')
print(f'Area of circle (sq. ft.): {area_of_circle}')