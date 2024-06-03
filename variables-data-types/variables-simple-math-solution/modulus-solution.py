# Modulus Solution

# Divide two numbers and use the modulus operator to get the remainder (if there
# is one)

# Get input
first_num = float(input('Enter your first number: (Example: 20.8)\n'))
second_num = float(input('Enter a second number: (Example:14)\n'))

# Process the input
answer = first_num % second_num

# Generate output (show the answer)
print(f'First number: {first_num}')
print(f'Second number: {second_num}')
print('NOTE: Zero (0) will display if the remainder was zero.')
print(f'Remainder: {answer}')