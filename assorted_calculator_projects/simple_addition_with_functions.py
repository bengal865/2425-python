# Anything missing here?




import time

# Define my function
def calculateSum(num1, num2):

	# The formula for doing the math
	theSum = num1 + num2
	
	# Return the sum of the two numbers to
	# the line where the function was called from
	
	return theSum
	
ordinal_nums = ["1st", "2nd", "3rd", "4th"]

# Call the function multiple times
# and display the answer to each calculation
for x in range(len(ordinal_nums)):

	firstNum = float(input ("Please enter your first number: "))
	
	secondNum = float(input ("Please enter your second number:"))
	
	myAnswer = calculateSum(firstNum, secondNum)
	
	time.sleep(1.5)
	print('Calculating...')
	print('Please wait...')
	time.sleep(2)

	print ("Answer to your", ordinal_nums[x],"calculation: " + str(myAnswer) + "\n\n")
        
print(' ***** END OF SCRIPT *****')
print(' ***** Thank you. *****')
