# Programmer: Bruce Provencher
# Date: 06 SEP 2014
# Project: Grocery Shopping

import time

welcomeMsg = "Hello, and welcome to Big Jim's Country Store!"
welcomeMsg2 = "We hope you enjoy shopping at our store today!"

print (welcomeMsg)
print (welcomeMsg2)
print()

# Prompt the user to enter the prices
# of five items s/he purchased at the grocery
# store

item1 = float(input("Enter the price of the first item: \n"))
item2 = float(input("Enter the price of the second item: \n"))
item3 = float(input("Enter the price of the third item: \n"))
item4 = float(input("Enter the price of the fourth item: \n"))
item5 = float(input("Enter the price of the fifth item: \n"))

itemSubtotal = item1 + item2 + item3 + item4 + item5

# Calculate the sales tax (at 6.00% in Michigan)
salesTaxRate = 0.06

salesTax = salesTaxRate * itemSubtotal

grandTotal = salesTax + itemSubtotal

print("Calculating your grocery bill.  Please wait...")

# Print the output after a short delay
time.sleep(3)
print ("Your subtotal (without sales tax): $" + "{0:,.2f}".format(itemSubtotal))
time.sleep(2)
print ("MI Sales Tax: $" + "{0:,.2f}".format(salesTax))
time.sleep(2)
print ("GRAND TOTAL: $" + "{0:,.2f}".format(grandTotal))
time.sleep(2)
print()
print("Thanks again for shopping at Big Jim's Country Store!")
print("Please visit us again soon!")
