# Calculate average score with functions

def get_scores():
    '''Function that prompts user to enter five quiz scores.'''
    counter = 0
    score = 0
    max_num_scores = 5
    scores = []
    while counter < max_num_scores:
        score = float(input('Enter a quiz score: (Example: 91)\n'))
        scores.append(score)
        counter += 1
    print(scores)
    return scores

def sum_scores(my_list):
    '''Function that finds the sum of the quiz scores in a list.'''
    return sum(my_list)

def calc_average_score(my_points, num_scores):
    '''Function that calculates the average quiz score.'''
    average = my_points / num_scores
    return average

def show_output(my_list, num_scores, my_average):
    '''Function that displays the quiz scores and the average quiz score.'''
    print(f'Your quiz scores: {my_list}')
    print(f'Number of quizzes taken: {num_scores}')
    print(f'Your average score: {my_average:,.2f}')

my_scores = []
my_scores = get_scores()    
total_points = sum_scores(my_scores)
#print(total_points)
average_score = calc_average_score(total_points, len(my_scores))
show_output(my_scores, len(my_scores), average_score)
