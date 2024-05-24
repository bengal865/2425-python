# Bruce Provencher
# 30 SEP 2022
# WHILE Loop with Counter

# Task 1

  # Add comments to explain what the counter variable is used for, and what +=1 does.
  # Add a comment that explains what the condition checks for.
  # Add a line of code inside the loop that outputs the counter variable every time the loop runs.  What do you notice about what happens to it each time the loop repeats?
  # Add a line of code after the loop that outputs the message 'The loop has finished'

# counter = 1

# while counter < 5:
#   print("This code is inside the loop!")
#   counter += 1


# Task 2

  # Add a line of code to the loop that subtracts one from the counter every time the loop runs  
  # Add a line of code after the loop that outputs 'Blast off'
  # EXTRA CHALLENGE - Adapt the code so that the user inputs the start value of the counter variable.

counter = 10
counter = int(input('Enter the starting value for your counter variable: (Example: 10)\n'))
print('####################################################################')

while counter > 0:
    print(counter)
    counter = counter - 1
print('Blast off!')


# Task 3

  # Write a program that uses a loop to output the seven times table up to 12 x 7 (HINT - use the counter variable and combine it with what you learned about maths with variables.)
  # Output the multiplied number as part of a sentence.  Example - '1 times 7 is 7'

  # EXTRA CHALLENGE - ask the user to input a number and output the multiplication table for the input.
# print('How high should your 7s times table go? Enter an integer from 1 - 12...\n')
# max_value = int(input())
# counter = 0

# while counter < max_value:
#     counter += 1
#     result = counter * 7
#     print(f'{counter} times 7 is {result}.')
    
    
# print('\nDone.')

# Cubes

# print('hello')
# upper_limit = int(input('Enter how many numbers Python should cube: (Example: 5)'))
# counter = 0

# while counter != upper_limit:
#     counter += 1
#     print(f'{counter**3}')

num1 = 2
num2 = 8

if num1 > num2:
  print(str(num1) + " is bigger.")
elif num1 != num2:
  print(str(num2) + " is bigger.")
else:
  print("Numbers are the same.")
    
    
