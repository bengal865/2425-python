prompt = '\nEnter the name of a city you have visited:'
prompt += '\nEnter \'quit\' when you are finished.\n'

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f'{city.title()} is one city I\'ve been to.')
		

