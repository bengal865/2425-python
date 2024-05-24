def calc_new_age(my_age):
	'''Function that adds ten years to the user's current age.'''
	new_age = my_age + 10	
	return new_age

	
	
# Get the user's age 
age = int(input('Please enter your age: (Example:17)\n')) 


# Send this value -- the user's age -- up to the function 
# The function parameter -- my_age -- catches the user's age, then adds 10 years to the user's age to come up with a new age for the user
# The new age is stored in the variable updated_age
updated_age = calc_new_age(age)


print(f'\nUser\'s age today: {age}')
print(f'User\'s age in 10 years: {updated_age}')
