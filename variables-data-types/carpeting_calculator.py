# Programmer: Bruce Provencher
# Date: 20 MAR 2018
# Project: Carpeting Calculator

# 1. asks the user to enter dimensions of a rectangular room (in feet)
# 2. calculates and displays how many square feet of carpet the user would need to carpet the entire room
# 3. calculates and displays how many square yards of carpet the user should purchase (where 1 square yard = 9 square feet)
# 4. calculates and displays the total cost of the carpet (assuming 1 square yard of carpet sells for $6.00)
# 5. thanks the user for using the program
# 6. tells the user to 'Press the ENTER key to exit.' (TIP: Use the input ( ) function to display this message on the screen.)

welcome_msg = """
Welcome to the Carpet Calculator!

This program will help you calculate the number of square
yards of carpet you need for your room.

Assuming new carpet costs $6.00 per square yard and that your state
tax rate is 6.00%, the calculator will also calculate and display the price
of your new carpet.

Please follow the prompts to continue...

"""
print(welcome_msg + "\n" + "\n")
room_width = float(input("Please enter the room width (in feet): \n"))
room_length = float(input("Please enter the room length (in feet): \n"))

# Calculate number of sq. ft. for room

square_ft = room_width * room_length

# Calculate number of SQUARE YARDS for the room

square_yards = square_ft / 9

# Calculate total cost of carpet (by square yards)

cost_per_square_yard = 6.00

subtotal = square_yards * cost_per_square_yard
sales_tax_rate = 0.06
sales_tax = subtotal * sales_tax_rate
grand_total = subtotal + sales_tax


# Convert cost per sq. yard into a string (for formatting purposes)
#cost_per_square_yard = str(cost_per_square_yard)

# Convert TOTAL COST into a string (for formatting purposes)
#total_cost = str(total_cost)

# Thank user for using the program
# Display output

print (f"Thank you for using the Carpet Calculator program.\n")

#print ("Number of SQUARE YARDS of carpet required: " + "{0:.2f}".format(square_yards))
#print ("Cost per square yard of carpet: $" + "{0:.2f}".format(cost_per_square_yard))
#print ("TOTAL COST: $" + "{0:.2f}".format(total_cost))

print (f"Carpet required [in square yards]: {square_yards:,.2f}")
print (f"Cost per square yard of carpet: ${cost_per_square_yard:,.2f}")
print (f"Order subtotal [before state sales tax]: ${subtotal:,.2f}")
print (f"Michigan Sales Tax: ${sales_tax:,.2f}")
print (f"YOUR TOTAL COST: ${grand_total:,.2f}")

# Exit program

input ("\n\nPlease press the ENTER key to exit.")
