# Passing Arguments Between Functions

def get_first_name():
    '''A function that prompts the user for his/her first name.'''
    fname = input('Please enter your first name: (Example: Mike)\n')
    return fname

def get_last_name():
    '''A function that prompts the user for his/her last name.'''
    lname = input('Please enter your last name: (Example: Robertson)\n')
    return lname

def build_greeting(first_name, last_name):
    '''Function that builds a greeting that includes the user's first and last name.'''
    print(f'Greetings, {first_name.title()} {last_name.title()}!')
    print('How are you?')

def main():
    '''Function that acts as a container for the different function calls.'''
    # Get and return user's first name
    user_fname = get_first_name()
    # Get and return user's last name
    user_lname = get_last_name()
    # Build custom greeting that includes the user's first and last name
    build_greeting(last_name=user_lname, first_name=user_fname)

# Call the main ( ) function
main()


# Challenge

# Write a script that uses five custom functions to 
# calculate and display the AREA of a rectangle
# Your output should also include the dimensions of the rectangle (length, width) with the correct units of measure and area (feet, square feet)

# Function 1: Get and return width of rectangle
# Function 2: Get and return length of rectangle
# Function 3: Calculate area of rectangle
# Function 4: Display the output
# Function 5: A main function that serves as a container for your function calls