# Programmer: Bruce Provencher
# Date: 14 JAN 2017
# Program: Restaurant class

# Define the Restuarant class
class Restaurant():
    """Representation of a generic restaurant"""
    
    def __init__(self, name, cuisine_type):
        """Initialize the attributes to describe the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Print the restaurant name and the type of cuisine it serves"""
        print("The name of the restaurant is " + self.name + ".")
        print("The type of cuisine served is " + self.cuisine_type + ".")
        
    def open_restaurant(self):
        """Tell the user the restaurant is open for business"""
        print("The restaurant is open for business! Enjoy your meal!")
        
# Create an instance called my_restaurant based on the Restaurant class
my_restaurant = Restaurant("The Roadrunner Inn", "Southwestern")

# Print the two attributes of the restaurant
print("Our restaurant is named " + my_restaurant.name + " and we serve homemade " + my_restaurant.cuisine_type + " cuisine.")
# Call both methods
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


