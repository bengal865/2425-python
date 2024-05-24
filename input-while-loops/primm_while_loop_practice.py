
# Task 1 - Add comments to explain which code is in the loop and will be repeated.

  # Explain the circumstances in which the loop will run.




# Task 2

  # Add a line of code to the loop that outputs an 'incorrect' message to the user and tells them what to do again.
  # Add a line of code to the loop that outputs an 'incorrect' message to the user, tells them what to do again and lets them re-input their number
  # Add a line of code AFTER the loop that ouputs a thank you message and repeats the number entered back to the user.  Example - 'Thank you, you typed 7'

# num1 = int(input("Enter a number 10 or less:\n"))


# while num1 > 10:
#     print('Incorrect! Please enter a number 10 or less!')
#     num1 = int(input('Enter a number 10 or less:\n'))
# print(f'Thank you! You entered the number: {num1}')
# Task 3

  # Write a program that stores a secret number in a variable (you decide the number and the name of the variable)
  # The user has to guess the secret number, the program should loop until they get it right.
  # Once the user has guessed correctly they get a congratulations message
secret_number = 5
print('Try to guess the secret number, which is between 1 (including 1) and 10 (also including 10).')
user_guess = int(input('Enter your guess:\n'))

while user_guess != secret_number:
    print('Incorrect! Please try again!')
    user_guess = int(input('Enter another guess:\n'))
print(f'Congratulations! You guessed the secret number, which was: {secret_number}')