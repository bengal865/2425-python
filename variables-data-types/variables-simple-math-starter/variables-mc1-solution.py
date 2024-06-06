# Abe Lincoln
# 20 JUN 20XX
# MC Variables & Data Types

import time

# Explain what script will do
print('''
This script will prompt you for two numbers.
      
Python will then calculate and display:
      - the square of the first number
      - the cube of the second number
''')
time.sleep(1) 

# Get input from user
first_num = float(input('Enter your first number: (Example: 8)\n'))
time.sleep(1)
second_num = float(input('Enter a second number: (Example: 3)\n'))
time.sleep(1)
print('Calculating...Please wait...')
time.sleep(2)
# Process
num1_squared = first_num ** 2
num2_cubed = second_num ** 3

# Display output
print(f'First number: {first_num}')
print(f'Second number: {second_num}\n')
print(f'{first_num} raised to the power of 2 is: {num1_squared}')
print(f'{second_num} raised to the power of 3 is: {num2_cubed}\n')
time.sleep(2)
print('Thank you for using my script!')
print('Have a good day!')

