

# 

number = 0.0
average = 0.0
running_total = 0.0
loop_count = 0

# 
user_numbers = []

# 
number = float(input("Please enter your number: (-999 to quit) \n"))

while number !=-999:
	
	# 
	loop_count += 1
	
	# 
	user_numbers.append(number)
	
	# 
	running_total = running_total + number
	
	# 
	average = running_total / loop_count
	
	# 
	number = float(input("Please enter another number: (-999 to quit) \n"))

# Display the output
print ("Your list of numbers is:\n")
print (user_numbers)
print (f"Average: {average:,.2f}")
print (f"Sum: {running_total:,.2f}\n")

