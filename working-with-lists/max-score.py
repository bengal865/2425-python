# Bruce Provencher
# 13 FEB 2021
# Use Functions to Get MAX Quiz Score

def get_max_score(scores):
	'''Function that returns the maximum score from a list of quiz scores.'''
	max_score = max(scores)
	return max_score
	
def populate_list():
	'''Function that uses a FOR loop to populate an empty list.'''
	quiz_scores = []
	for x in range(1, 6):
		percentage = float(input(f'Please enter quiz score #{x}: (Example: 85.00)\n'))
		quiz_scores.append(percentage)
	return quiz_scores
	
def main():
	updated_scores = populate_list()
	print('You entered the following quiz scores:')
	print(updated_scores)
	my_max_score = get_max_score(updated_scores)
	print(f'Your maximum score: {my_max_score:,.2f}')

if __name__ == '__main__':
	main()
