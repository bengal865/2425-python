# Math with Lists

quiz_scores = [99, 87, 91, 72, 77]

# # Task 1: Use variables, the len ( ) function and the sum ( ) function to calculate
# # and display the AVERAGE quiz score (for the quiz_scores list)

# average = sum(quiz_scores) / len(quiz_scores)
# print(average)

# Task 2: Use a FOR loop, a counter variable, any Python functions and variables you 
# need to calculate and display the AVERAGE quiz score (using the quiz_scores list)
# count = 1
# total = 0
# average = 0
# for index in range(len(quiz_scores)):
#     total += quiz_scores[index]
#     count += 1
# average = total / count
# print(f'Average quiz score: {average}')
# print()



scores1 = [88, 92, 90, 75, 62]


scores2 = [62, 70, 78, 99, 100]











print(f"The average of the scores is {sum(scores1 + scores2) / len(scores1 + scores2)}")
# # How could we get Python to multiply the number pairs from scores1 and scores2?

# # HINT: Use a FOR loop, index numbers, and the len( ) and range ( ) functions.
# import random
# scores = []
# score = 0
# random_num = 0
# for i in range(5):
#     random_num = random.randint(0, 101)
#     scores.append(random_num)
# print(scores)