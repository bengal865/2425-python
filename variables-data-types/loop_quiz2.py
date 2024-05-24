# Bruce Provencher
# 10 OCT 2022
# Intro to Iteration in Python

# Declare and initialize variables
score = 0
max_scores = 6
count = 0
total = 0
average = 0

first_name = '' # Empty or null string

# Get first name from user for custom greeting
first_name = input('Please enter your first name: (Example: Mike)\n').title()

print(f'Hello, {first_name}! This script will calculate your average quiz score.')
print()

# Prompt user for the six quiz scores
while count < max_scores:
    score = int(input('Enter a quiz score:\n'))
    total = total + score
    count = count + 1
    # Calculate the average score
average = total / count

# Display the average score
print(f'Your quiz average: {average}')
print()
print('Thank you, and goodbye!')