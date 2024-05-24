# Bruce Provencher
# Simple Python Quiz Game

import time

def get_first_name():
    '''Function that prompts user for his/her first name.'''
    fname = input('Please enter your first name:\n')
    return fname

def show_game_intro(fname):
    '''Function that welcomes the user to the game and
    shows a customized welcome message on the screen.'''
    print(f'Welcome, {fname} to a simple Python trivia game!\n')
    time.sleep(1.5)
    print('You will answer five questions, and your score will')
    print('be displayed once the game ends.\n')
    time.sleep(1.5)
    print('Good luck!')
    
def main():
	
	# Create my list of questions and answers

	questions = [
		'What is the capital of Norway?',
		'In what year did the U.S. Civil War end?',
		'In the United States, the Four Corners includes the states of New Mexico, Arizona, Colorado and __________?',
		'How many inches are in one mile?',
		'Which continent was a former prison colony?'
	]

	answers = [
		'oslo',
		'1865',
		'utah',
		'63360',
		'australia'
	]

	# Also create two lists, one for the questions I answered correctly,
	# the other for the questions I DID NOT answer correctly
	correct_answers = []
	incorrect_answers = []

	# Create te variables I need to keep track of my score and
	# the number of correct and incorrect answers
	points = 0
	num_correct_answers = 0
	num_incorrect_answers = 0
	# Use the len ( ) function to count the number of questions in my list
	# of questions
	points_possible = len(questions * 2)
	
	# Calling the functions

	first_name = get_first_name()
	first_name = first_name.title()
	show_game_intro(first_name)
	
	# Display each question from the list of questions

	for question in questions:
		print(question)

		# User enters his/her answer here...
		user_answer = input('Enter your answer:\n\n')

		# Check the user's answer against my list of answers
		if user_answer.lower() in answers:
			correct_answers.append(question)
			num_correct_answers = num_correct_answers + 1
			points = points + 2
		else:
			incorrect_answers.append(question)
			num_incorrect_answers = num_incorrect_answers + 1
	# Show the questions I answered correctly
	for correct_answer in correct_answers:
		print(f'Correct answer: {correct_answer}\n\n')
		
	time.sleep(2)
	# Show which questions I did not answer correctly
	for incorrect_answer in incorrect_answers:
		print(f'Incorrect answer: {incorrect_answer}\n\n')
    
    # Show my stats (score, etc.)
	time.sleep(2)
	print('Your final score:\n')
	time.sleep(2)
	print(f'Correct answers: {num_correct_answers}')
	time.sleep(2)
	print(f'Incorrect answers: {num_incorrect_answers}')
	time.sleep(2)
	print(f'Number of questions: {len(questions)}')
	time.sleep(2)
	print(f'Your score: {(points / points_possible) * 100:,.2f}%')
	time.sleep(2)
	print(f'Thanks for playing today, {first_name}!')
	
if __name__ == '__main__':
	main()


