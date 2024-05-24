# Bruce Provencher
# 07 OCT 2022
# While Loop Demonstration

scores = [98, 97, 80, 82, 88, 86]

num_items = len(scores)

count = 0
total = 0
while count != num_items:
    total += scores[count]
    count += 1
average = total / count
print(average)

score1 = input('Enter your quiz score:')
score1 = float(score1)

score2 = input('Enter your quiz score:')
score2 = float(score1)

score3 = input('Enter your quiz score:')
score3 = float(score1)

score4 = input('Enter your quiz score:')
score4 = float(score1)

score5 = input('Enter your quiz score:')
score5 = float(score1)

num_scores = 5

total = score1 + score2 + score3 + score4 + score5

average = total / num_scores
print(f'Total Points: {total}')
print(f'Average Score: {average}')

# Pizza Toppings 
prompt = 'Enter a topping for your pizza.  (Example: mushrooms)'
prompt += 'To quit this script, enter q for quit.\n'

message = ''
while message != 'q':
    message = input(prompt)

    if message != 'q':
        print(f'Adding {message} to your pizza!')

# Flag variable 
prompt = 'Enter the name of a city you\'ve visited.  (Example: Grand Rapids)'
prompt += 'To quit this script, enter the word quit.\n'

keep_looping = True

while keep_looping:
    city = input(prompt)

    if city == 'quit':
        keep_looping = False
    else:
        print(f'I\'d love to go back to {city.title()} next year!')
