# Bruce Provencher
# 23 MAY 2022
# Simple Calculator

import sys
 
def addition(num1, num2):
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")
     
def multiplication(num1, num2):
    mul = num1 * num2
    print(f"{num1} * {num2} = {mul}")
     
def subtraction(num1, num2):
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")
     
def division(num1, num2):
    try:
        div = num1 / num2
    except ZeroDivisionError as e:
        print("Exception raised: ", e)
    else:
        print("{} / {} = {:.2f}".format(num1,num2,div))
 
print("""
Please enter:
+ for addition
- for subtraction
* for multiplication
/ for division
q to quit
""")
 
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter a second number:"))
 
while True:
    operation = input("\nEnter an operator(+,-,*,/,q):")
 
    if operation == "+":
        addition(num1, num2)
         
    elif operation == "*":
        multiplication(num1, num2)
         
    elif operation == "-":
        subtraction(num1, num2)
         
    elif operation == "/":
        division(num1, num2)
         
    elif operation == "q":
        print("Exiting the calculator!")
        sys.exit()
         
    else:
        print("Incorrect operator! Please enter (+,-,*,/,q) only!")