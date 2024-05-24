# Programmer: Bruce Provencher
# Date: 20 May 2019
# Reading Multiple Files &  Exception Handling

stories = ['dogs.txt', 'cats.txt']
for story in stories:
	try:			
		with open(story) as file_object:
			content = file_object.read().splitlines() # The splitlines() method splits a string into a list. The splitting is done at line breaks
				
	except FileNotFoundError:
		print(f"Sorry, but the file you requested, {story}, does not exist or can't be located.")

	else:
		if story == stories[0]:
			print("A few dog names:")	
		else:
			print("And some cat names:")
		for line in content:
			print(line.strip('"')) # Single quotes containing just one double quote
