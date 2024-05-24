# Bruce Provencher
# 25 MAY 2021
# Dictionary: Add User Input to Dictionary

# Create empty dictionary
rental_properties = {}

# Set flag variable to indicate we are taking
# applications for rental properties
rental_available = True

while rental_available:
    # Prompt user for their username and address of property
    username = input('Please enter your username:\n')
    property_address = input('Enter the street address of the available rental property: (Example: 287 Renslow Avenue)\n')
    # Format property address (title case)
    property_address = property_address.title()
    
    # Store responses in the dictionary
    rental_properties[username] = property_address
    
    # Is anyone else interested in renting one of the rental properties?
    repeat = input('\nDo you know anyone else interested in renting their property? (y\n):\n')
    if repeat in ['n', 'no']:
        rental_available = False
    else:
        continue
    
 
#print(rental_properties.keys())
#print(rental_properties.values())

print('\n--- Properties to Rent --- ')  
for username, property_address in rental_properties.items():
    print(f'{username.title()} currently has a rental at {property_address.title()} for rent.')
    
        
