# Bruce Provencher
# 10 OCT 2022
# Intro to Iteration in Python

# Declare and initialize variables
quiz1 = 0
quiz2 = 0
quiz3 = 0
quiz4 = 0
quiz5 = 0
quiz6 = 0

num_quiz_scores = 6
total = 0
average = 0

# Get first name from user for custom greeting
first_name = input('Please enter your first name: (Example: Mike)\n').title()

print(f'Hello, {first_name}! This script will calculate your average quiz score.')
print()

# Prompt user for the six quiz scores
quiz1 = float(input('Enter a quiz score: (Example: 84)\n'))
quiz2 = float(input('Enter a quiz score: (Example: 84)\n'))
quiz3 = float(input('Enter a quiz score: (Example: 84)\n'))
quiz4 = float(input('Enter a quiz score: (Example: 84)\n'))
quiz5 = float(input('Enter a quiz score: (Example: 84)\n'))
quiz6 = float(input('Enter a quiz score: (Example: 84)\n'))

# Calculate sum of quiz scores, then the average score
total = quiz1 + quiz2 + quiz3 + quiz4 + quiz5 + quiz6

average = total / num_quiz_scores

# Display the individual quiz scores, then the average score
print('Here are your individual quiz scores:')
print(f'{quiz1} {quiz2} {quiz3} {quiz4} {quiz5} {quiz6} ')
print()
print(f'And your average is: {average}')
print()
print('Thank you, and goodbye!')