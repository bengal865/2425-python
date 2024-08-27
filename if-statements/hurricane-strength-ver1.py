def get_hurricane_category(wind_speed):
    if wind_speed >= 74 and wind_speed <= 95:
        return "Category 1"
    elif wind_speed >= 96 and wind_speed <= 110:
        return "Category 2"
    elif wind_speed >= 111 and wind_speed <= 130:
        return "Category 3"
    elif wind_speed >= 131 and wind_speed <= 155:
        return "Category 4"
    elif wind_speed >= 156:
        return "Category 5"
    else:
        return "Not a hurricane!"
    
wind_speed = float(input("Enter the wind speed (mph):\n"))
category = get_hurricane_category(wind_speed)

print(f"Hurricane category: {category}")

# Rewritten without using a function
wind_speed = float(input("Enter the wind speed (mph):\n"))

if wind_speed >= 74 and wind_speed <= 95:
    category = "Category 1"
elif wind_speed >= 96 and wind_speed <= 110:
    category = "Category 2"
elif wind_speed >= 111 and wind_speed <= 130:
    category = "Category 3"
elif wind_speed >= 131 and wind_speed <= 155:
    category = "Category 4"
elif wind_speed >= 156:
    category = "Category 5"
else:
    category = "Not a hurricane!"

print(f"Hurricane category: {category}")