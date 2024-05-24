#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Bruce Provencher
# Project: Carpeting Calculator
# Date: 17 NOV 2012

# carpetcalculator.py
# Calculates how much carpet is needed to cover a room

# width represents the room's width
# length represents the room's length

# Create the variables needed for this project

# Use the raw_input function to collect a string value
# The string value in this case will be the name of the customer

print ("Please enter your first name: "),
customer = input()

#customer = raw_input ("Enter your first name, please!")

# Ask user to enter room width
# Assign input to the variable named width

print ("Enter the WIDTH of the room in feet:  ")
width = float(input())


# Ask user to enter room length
# Assign input to the variable named length

print ("Enter the LENGTH of the room in feet: ")
length = float(input())

# Set up the formula to calculate the number of square feet of carpet needed
# to cover the room

area = width * length

# Display the output 
# Thank customer and display results of calculation

print ('Hello, '+ customer + '!')
print ('Thank you for your order today!')
print ('To carpet your room, ' + customer + ', you\'ll need ', float(area), 'square feet of carpet!')
