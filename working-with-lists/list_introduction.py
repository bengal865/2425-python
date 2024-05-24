# Bruce Provencher
# 18 OCT 2022
# List Observations

am_students = ['Matt', 'Dillan', 'Elisabeth', 'Destiny', 'Maddox']
pm_students = ['Mike', 'Peyton', 'Cameron', 'Alexander', 'Noe']
all_students = [am_students, pm_students]

# for x in range(len(am_students)):
#     if am_students[x] in all_students[0][x]:
#         print(f'{all_students[0][x]} attends the AM session at Career Tech.')
#     if pm_students[x] in all_students[1][x]:
#         print(f'{all_students[1][x]} attends the PM session at Career Tech.')
# print()
# print('End of FOR loop.')
# print(all_students[0][3])
# example_student = 'mike'
# example_student = example_student.title()

# if example_student in all_students[0]:
#     print(f'{example_student.title()} is an AM student.')
# elif example_student in all_students[1]:
#     print(f'{example_student.title()} is a PM student.')
# else:
#     print(f'{example_student.title()} is not a Career Tech student.')

scores1 = [90, 72, 60]
scores2 = [50, 40, 30]

for index in range(len(scores1)):
    print(f'{scores1[index]} X {scores2[index]} = {scores1[index] * scores2[index]}')


