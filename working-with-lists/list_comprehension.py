# newlist = [num for num in range(0, 52, 2)]
# print(newlist)

# newlist_squares = [num ** 2 for num in newlist]
# print(newlist_squares)

# https://www.w3schools.com/python/python_lists_comprehension.asp

students = ['Smith', 'Jenkins', 'Haines', 'McDonald', 'Hartford', 'Clark', 'Hansen', 'Robertson']
selected_students = []

for student in students:
    if 'Ha' in student:
        selected_students.append(student)
print(selected_students)