# Project: While Loop / Let User Choose When to Quit

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter \'quit\' to end the script.\n\n'

# Empty message to start with
message = ''
while message != 'quit':
	message = input(prompt)
	
	# Display message as long as the user doesn't
	# choose to quit the script
	if message != 'quit':
		print(message)
	
