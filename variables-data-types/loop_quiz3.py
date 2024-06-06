num_quiz_scores = 6
total = 0

# Get first name from user for custom greeting
first_name = input('Please enter your first name: (Example: Mike)\n').title()

print(f'Hello, {first_name}! This script will calculate your average quiz score.')
print()

# Prompt user for the six quiz scores using a for loop
quiz_scores = []
for i in range(num_quiz_scores):
  quiz_score = float(input(f'Enter a quiz score {i+1} of {num_quiz_scores}: (Example: 84)\n'))
  quiz_scores.append(quiz_score)

# Calculate sum and average
# total = sum(quiz_scores)
average = (sum(quiz_scores)) / num_quiz_scores

# Display the individual quiz scores, then the average score
print('Here are your individual quiz scores:')
print(*quiz_scores)  # Use unpacking for cleaner output
print()
print(f'And your average is: {average:.2f}')
print()
print(f'Thank you, {first_name} and goodbye!')
