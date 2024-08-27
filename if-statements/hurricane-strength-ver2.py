# Define lists for minimum and maximum wind speeds for each category
min_wind_speeds = [74, 96, 111, 131, 156]
max_wind_speeds = [95, 110, 130, 155, float('inf')]  # Use 'inf' for the last maximum wind speed

# Get user input
wind_speed = float(input("Enter the wind speed (mph):\n"))

# Determine the category
category = "Not a hurricane!"
for i in range(len(min_wind_speeds)):
    if min_wind_speeds[i] <= wind_speed and wind_speed <= max_wind_speeds[i]:
        category = f"Category {i + 1}"
        break

# Print the result
print(f"Hurricane category: {category}")