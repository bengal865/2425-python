# Bruce Provencher
# 10 OCT 2022
# Movie Tickets (7-5 PCC)

# Declare and initialize variables
age = 0
ticket_price = 0

# Prompt user for their age
age = int(input('Please enter your age: (Example: 17)\n'))

# Check user's age against the conditions, one at a time
if age < 3:
    print(f'You are under the age of 3, so your ticket is free!\n')
elif age >= 3 and age <= 12:
    ticket_price = 10
    print(f'You ticket costs ${ticket_price:,.2f}!\n')
elif age > 12:
    ticket_price = 15
    print(f'You are older than 12, so your ticket costs ${ticket_price:,.2f}!\n')
