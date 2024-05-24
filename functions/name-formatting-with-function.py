# Bruce Provencher
# 13 FEB 2021
# Name Formatting Using a Function

def get_formatted_name(first_name, last_name, middle_name = ''):
	'''Return a full name, neatly formatted.'''
	if middle_name:
		full_name = f'{first_name} {middle_name} {last_name}'
	else:
		full_name = f'{first_name} {last_name}'
		
	return full_name.title()

def main():
	student = get_formatted_name('James', 'McMurphy', 'Allen')
	print(f'Your nicely formatted name is: {student}')
	
if __name__ == '__main__':
	main()
