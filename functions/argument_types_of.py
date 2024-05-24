# Programmer: Bruce Provencher
# Date: 11 NOV 2018
# Projects: Types of Arguments in Python

def customize_shirt(size, message):
    """Display info about the T-shirt"""
    print("T-shirt size: " + size)
    print("Message on shirt: " + message)


# Call the function we need using positional arguments
customize_shirt("Large", "Python rocks!")

# Call function using KEYWORD arguments
customize_shirt(message = "Welcome to the CTC!", size="Small")

# Baggy T-Shirts Project
# All T-shirts are large by default
# Default message reads: "Python rocks, bro!"
# Set the default values for the two parameters

def baggy_shirt_info(size = "Large", message = "Python rocks, bro!"):
    """Display info about the baggy T-shirt"""
    print("T-shirt size: " + size)
    print("Message on shirt: " + message)

# Call function using some keyword arguments again
baggy_shirt_info()
baggy_shirt_info(size="Medium")
baggy_shirt_info(size="XL", message = "Welcome to the 2018 Gamers' Convention!")

# Going International Project
def describe_city(city, country="Canada"):
    print("City name: " + city)
    print(city + " is located in " + country + ".")

describe_city("Halifax")
describe_city("Toronto")
describe_city("Vienna", "Austria")
describe_city("Hamburg", "Germany")
describe_city("Rome", "Italy")
