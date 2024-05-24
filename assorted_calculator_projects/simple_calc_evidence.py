'''
Programmer: Mya Tooker
Date: 30 September 2020
Project: Simple Calc Evidence
'''

import time

def find_diff(num1, num2):
    the_diff = num1 - num2
    return the_diff
def find_pro(num1, num2):
    the_pro = num1 * num2
    return the_pro
def find_quo(num1, num2):
    the_quo = num1 / num2
    return the_quo

first_name = input("Please enter your first name: \n")
time.sleep(1)
print(f"Welcome, {first_name}!")
time.sleep(1)

num1 = float(input(f"Please enter your first number, {first_name}: \n"))
time.sleep(1)
num2 = float(input(f"Please enter a second number, {first_name}: \n"))
time.sleep(1)

print(f"Python will now do subtraction for you, {first_name}...")
print(f"{num1} - {num2} = {str(find_diff(num1, num2))}")
time.sleep(1)

print(f"Python will now do multiplication for you, {first_name}...")
print(f"{num1} * {num2} = {str(find_pro(num1, num2))}")
time.sleep(1)

print(f"Python will now do division for you, {first_name}...")
print(f"{num1} / {num2} = {str(find_quo(num1, num2))} \n")
time.sleep(1)

print(f"Thank you for using my simple calculator! Adios, {first_name}!")