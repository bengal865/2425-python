# Math with Python Lists

# quiz_scores = [99, 87, 91, 72, 77]

# Task 1: Use variables, the len ( ) function and the sum ( ) function to calculate
# and display the AVERAGE quiz score (for the quiz_scores list)



# Task 2: Use a FOR loop, a counter variable, any any Python functions and varialbes you need to calculate and display the AVERAGE quiz score (using the quiz_scores list)

# counter = 1
# total = 0
# average = 0
# for index in range(len(quiz_scores)):
#     total += quiz_scores[index]
#     counter += 1
# average = total / len(quiz_scores)
# print(f'Average: {average}')



scores1 = [88, 92, 90, 75, 62]
scores2 = [62, 70, 78, 99, 100]

# How could we get Python to multiply the number pairs from scores1 and scores2?

# HINT: Use a FOR loop, index numbers, and the len( ) and range ( ) functions.

for index in range(len(scores1)):
    answer = scores1[index] * scores2[index]
    print(f'{scores1[index]} times {scores2[index]} = {answer}.')
print('End of loop.')