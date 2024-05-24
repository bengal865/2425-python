# Programmer: Bruce Provencher
# Date: 19 SEP 2014
# Project: Testing a Python Module (modular.py)

# Import the module we created into this program
# using the keyword 'import'

import my_module

celsius = float(input("Input a temperature in Celsius: \n"))

fahrenheit = my_module.celsiusToFahr(celsius)

print ("That's", fahrenheit, "degrees Fahrenheit.")

