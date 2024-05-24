"""

# Programmer: Jack Perry    
# Date: 02 OCT 2020
# Project: Making a T-Shirt

"""

# First time using positional arguments to make a shirt

def make_shirt(size="large", message="Python rocks, dude!"):
    print(f"\nYour shirt's size is: {size}")
    print(f"\nThe message included is: {message}\n")

make_shirt(size='large')
make_shirt(size='medium')
make_shirt(size='small', message='Gamer moment.')

size = input('Please enter the size of your desired shirt: ')
message = input('Please enter the desired message on your shirt: ')

print (make_shirt(size, message))